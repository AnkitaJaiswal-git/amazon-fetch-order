pipeline {
    agent any

    environment {
        AMAZON_EMAIL = credentials('amazon-email')
        AMAZON_PASSWORD = credentials('amazon-password')
    }

    stages {
        stage('Install Google Chrome') {
            steps {
                sh '''
                    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/google.gpg
                    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
                    sudo apt-get update
                    sudo apt-get install -y google-chrome-stable
                '''
            }
        }
        
        stage('Install System Packages') {
            steps {
                sh '''
                    sudo apt-get update
                    sudo apt-get install -y python3-venv python3-full wget unzip curl
                '''
            }
        }

        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/AnkitaJaiswal-git/amazon-fetch-order.git', branch: 'main'
            }
        }
        

        stage('Set Up Python Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv amazonenv
                    amazonenv/bin/pip install --upgrade pip
                    amazonenv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Order Fetcher') {
            steps {
                sh '''
                    amazonenv/bin/python fetch_amazon_orders.py "$AMAZON_EMAIL" "$AMAZON_PASSWORD"
                '''
            }
        }
    }
}
