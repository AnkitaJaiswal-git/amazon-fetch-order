pipeline {
    agent any

    environment {
        AMAZON_EMAIL = credentials('amazon-email')
        AMAZON_PASSWORD = credentials('amazon-password')
    }

    stages {
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
                    source amazonenv/bin/activate
                    amazonenv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Install ChromeDriver') {
            steps {
                sh '''
                    wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
                    unzip chromedriver_linux64.zip
                    chmod +x chromedriver
                    sudo mv chromedriver /usr/local/bin/
                '''
            }
        }

        stage('Run Order Fetcher') {
            steps {
                sh '''
                    source amazonenv/bin/activate
                    amazonenv/bin/python3 fetch_amazon_orders.py "$AMAZON_EMAIL" "$AMAZON_PASSWORD"
                '''
            }
        }
    }
}
