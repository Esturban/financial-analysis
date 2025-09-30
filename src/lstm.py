from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import warnings
warnings.filterwarnings('ignore')

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, Masking
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
import tensorflow as tf
import numpy as np

#Training the model - Developed into a function handle each of the folds
def train_lstm_model(X_train, y_train, X_val, y_val, config):
    """Train a single LSTM model with given configuration"""
    model = Sequential()
    model.add(Masking(mask_value=0.0, input_shape=(config['seq_length'], 1)))

    # Build layers based on configuration
    for i, units in enumerate(config['hidden_layers']):
        return_seq = i < len(config['hidden_layers']) - 1
        model.add(LSTM(units,
                      return_sequences=return_seq,
                      dropout=config['dropout'],
                      recurrent_dropout=config['recurrent_dropout']))

    model.add(Dense(config['dense_layers']))
    model.add(Dense(1))

    optimizer = Adam(clipvalue=config['clip_value'], learning_rate=config['learning_rate'])
    model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mae'])

    early_stop = EarlyStopping(
        monitor='val_loss',
        patience=config['patience'],
        restore_best_weights=True
    )

    history = model.fit(
        X_train, y_train,
        batch_size=config['batch_size'],
        epochs=config['epochs'],
        validation_data=(X_val, y_val),
        callbacks=[early_stop],
        verbose=0
    )

    return model, history

#Creating the method evaluating the metrics of the model between actual vs. predictions
def evaluate_model(model, X_test, y_test, scaler):
    """Evaluate model and return predictions and metrics"""
    predictions_scaled = model.predict(X_test, verbose=0)
    predictions = scaler.inverse_transform(predictions_scaled)
    y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

    mse = mean_squared_error(y_test_actual, predictions)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test_actual, predictions)
    r2 = r2_score(y_test_actual, predictions)

    return predictions, {
        'RMSE': rmse,
        'MAE': mae,
        'R2': r2,
        'MSE': mse
    }