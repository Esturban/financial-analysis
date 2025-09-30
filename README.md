# Stock Market Analysis & Prediction using LSTM

A comprehensive Python-based project for analyzing technology stocks and predicting future prices using Long Short-Term Memory (LSTM) neural networks.

![Stock Market Analysis](https://placehold.co/600x400?text=Stock+Market\nAnalysis)

## 📊 Project Overview

This project performs in-depth analysis of major technology stocks including Apple (AAPL), Google (GOOG), Microsoft (MSFT), Amazon (AMZN), Tesla (TSLA), and NVIDIA (NVDA). The analysis covers historical price movements, technical indicators, risk assessment, correlation studies, and implements LSTM-based price prediction models.

### Key Questions Addressed

1. **Price Analysis**: What was the change in stock price over time?
2. **Return Analysis**: What was the daily return of stocks on average?
3. **Trend Analysis**: What were the moving averages of various stocks?
4. **Correlation Study**: What was the correlation between different stocks?
5. **Risk Assessment**: How much value do we put at risk by investing in a particular stock?
6. **Price Prediction**: How can we predict future stock behavior using LSTM?

## 🚀 Features

- **Historical Data Collection**: Automated download of stock data using Yahoo Finance API
- **Technical Analysis**: Comprehensive technical indicators using TA-Lib
- **Data Visualization**: Interactive plots using Matplotlib and Seaborn
- **Statistical Analysis**: Risk metrics including volatility and Value at Risk (VaR)
- **Correlation Analysis**: Inter-stock relationship studies
- **LSTM Prediction**: Deep learning models for stock price forecasting
- **Performance Evaluation**: Model metrics including RMSE, MAE, and R² scores

## 🛠 Tech Stack

### Core Dependencies
- **Data Processing**: `pandas`, `numpy`
- **Financial Data**: `yfinance`, `pandas-datareader`
- **Machine Learning**: `scikit-learn`, `tensorflow`
- **Technical Analysis**: `TA-Lib`
- **Visualization**: `matplotlib`, `seaborn`
- **Deep Learning**: `keras`

### Development Tools
- **Jupyter Notebook**: Interactive analysis environment
- **Python 3.7+**: Core programming language

## 📁 Project Structure

```
finance/
│
├── stock-market-analysis-prediction-using-lstm.ipynb  # Main analysis notebook
│
├── src/
│   ├── __init__.py                    # Package initialization
│   ├── utils.py                       # Data collection and plotting utilities
│   └── lstm.py                        # LSTM model implementation
│
├── analysis/
│   └── tech/
│       └── eda.ipynb                   # Exploratory data analysis (technical)
│
├── requirements.txt                   # Python dependencies
├── finance.code-workspace             # VS Code workspace configuration
└── README.md                          # Project documentation
```

## 🏃‍♂️ Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Active internet connection (for data download)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Esturban/financial-analysis.git finance
   cd finance
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python -c "import yfinance, tensorflow, talib; print('All dependencies installed successfully!')"
   ```

## 📖 Usage

### Running the Analysis

1. **Open the main notebook**
   ```bash
   jupyter notebook stock-market-analysis-prediction-using-lstm.ipynb
   ```

2. **Execute cells sequentially** to perform:
   - Data collection from Yahoo Finance
   - Technical analysis and visualization
   - Risk assessment calculations
   - LSTM model training and prediction

### Key Functions

#### Data Collection (`src/utils.py`)
- `dl_combined_data()`: Downloads historical data for multiple tickers
- `plotting_var()`: Creates comparative visualizations
- `create_sequences()`: Prepares data for LSTM training

#### LSTM Implementation (`src/lstm.py`)
- `train_lstm_model()`: Trains LSTM models with configurable parameters
- `evaluate_model()`: Evaluates model performance with multiple metrics

## 📊 Analysis Coverage

### Stocks Analyzed
- **AAPL** - Apple Inc.
- **GOOG** - Alphabet Inc. (Google)
- **MSFT** - Microsoft Corporation
- **AMZN** - Amazon.com Inc.
- **TSLA** - Tesla Inc.
- **NVDA** - NVIDIA Corporation

### Time Period
- 5 years of historical data (automatically calculated from current date)

### Technical Indicators
- Moving Averages (SMA, EMA)
- Relative Strength Index (RSI)
- Moving Average Convergence Divergence (MACD)
- Bollinger Bands
- Volume indicators

## 🔧 Configuration

### LSTM Model Parameters
- **Sequence Length**: 60 days (configurable)
- **Hidden Layers**: Configurable architecture
- **Dropout Rate**: Prevents overfitting
- **Early Stopping**: Prevents overtraining
- **Learning Rate**: Optimized for convergence

### Data Parameters
- **Training Split**: 80% training, 20% testing
- **Validation Split**: 20% of training data
- **Feature Scaling**: MinMax normalization

## 📈 Results & Performance

The project includes comprehensive evaluation metrics:
- **Root Mean Square Error (RMSE)**
- **Mean Absolute Error (MAE)**
- **R-squared (R²) Score**
- **Mean Squared Error (MSE)**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Yahoo Finance** for providing comprehensive financial data
- **yfinance library** for Python integration
- **TensorFlow/Keras** for deep learning framework
- **TA-Lib** for technical analysis functions

## 📞 Support

For questions, issues, or contributions, please:
- Open an issue on GitHub
- Contact the maintainers
- Check the documentation in the notebook

---

**Note**: This project is for educational and research purposes. Always conduct your own analysis before making investment decisions. Past performance does not guarantee future results.
