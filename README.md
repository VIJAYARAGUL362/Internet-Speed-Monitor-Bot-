# Internet Speed Monitor Bot 🚀

An automated bot that monitors your internet speed and posts complaints to Mastodon when your ISP isn't delivering the speeds you're paying for.

**Day 51 Project** from [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu

## 📋 Features

- Automated speed testing using Speedtest.net
- Real-time upload and download speed measurement
- Automatic posting to Mastodon when speeds are below promised levels
- Persistent browser sessions using Chrome profiles
- Configurable speed thresholds

## 🛠️ Technologies Used

- **Python 3.x**
- **Selenium WebDriver** - Browser automation
- **Chrome/ChromeDriver** - Web browser control
- **python-dotenv** - Environment variable management

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/internet-speed-monitor-bot.git
   cd internet-speed-monitor-bot
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver**
   - Visit [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/)
   - Download the version matching your Chrome browser
   - Extract and note the path

4. **Configure environment variables**
   - Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```
   - Edit `.env` and add your credentials:
   ```
   MASTODON_ACCOUNT_EMAIL=your_email@example.com
   MASTODON_ACCOUNT_PASSWORD=your_password
   ```

5. **Update ChromeDriver path**
   - Open `main.py`
   - Update `CHROME_DRIVER_PATH` to your ChromeDriver location

## ⚙️ Configuration

Edit the following variables in `main.py`:

```python
PROMISED_UP = 150      # Your promised upload speed (Mbps)
PROMISED_DOWN = 30     # Your promised download speed (Mbps)
```

## 🚀 Usage

Run the bot:
```bash
python main.py
```

The bot will:
1. Open Speedtest.net
2. Run a speed test
3. Log into Mastodon
4. Post the results with a complaint message

## 📝 How It Works

1. **Speed Test**: Navigates to Speedtest.net and initiates a test
2. **Data Collection**: Waits for upload/download speeds to be measured
3. **Social Media Post**: Logs into Mastodon and posts the results
4. **Session Persistence**: Saves browser profile to avoid repeated logins

## 🔒 Security Notes

- **NEVER commit your `.env` file** - It contains sensitive credentials
- The `.env` file is already in `.gitignore`
- Consider using Mastodon API tokens instead of password authentication
- Store ChromeDriver path as an environment variable for better security

## 📸 Example Output

```
button is clicked
Checking upload speed...
12.5
Checking download speed...
upload speed: 12.5 Mbps
download speed: 8.3 Mbps
Posting to Mastodon...
```

## 🐛 Troubleshooting

**Chrome/ChromeDriver version mismatch**
- Ensure ChromeDriver version matches your Chrome browser version

**Element not found errors**
- Website layouts may change; update selectors in code
- Increase wait times if you have a slow connection

**Login fails**
- Verify credentials in `.env` file
- Check if Mastodon requires 2FA (not currently supported)

## 🛣️ Roadmap

- [ ] Add scheduling (run tests periodically)
- [ ] Support for multiple ISPs
- [ ] Email notifications
- [ ] Data logging and visualization
- [ ] API-based Mastodon posting (more secure)
- [ ] Support for other social platforms

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This bot is for educational purposes. Please:
- Use responsibly and respect Mastodon's terms of service
- Don't spam or abuse the platform
- Be aware of rate limits on social media platforms

## 👤 Author

Your Name - [@yourhandle](https://mastodon.social/@yourhandle)

Project Link: [https://github.com/yourusername/internet-speed-monitor-bot](https://github.com/yourusername/internet-speed-monitor-bot)

## 🙏 Acknowledgments

- **Dr. Angela Yu** - [100 Days of Code: Python Bootcamp](https://www.udemy.com/course/100-days-of-code/)
- [Speedtest.net](https://www.speedtest.net/) for speed testing
- [Mastodon](https://mastodon.social/) for the social platform
- [Selenium](https://www.selenium.dev/) for browser automation

## 📚 Learning Journey

This project is part of my 100 Days of Code challenge, focusing on:
- Web automation with Selenium
- Working with environment variables
- Browser interaction and DOM manipulation
- Social media automation
- Real-world problem solving
