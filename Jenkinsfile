pipeline {
    agent { label 'MandS' } 

    environment {
        AMAZON_EMAIL = credentials('amazon-email')
        AMAZON_PASSWORD = credentials('amazon-password')
    }

    stages {
        stage('Install Python') {
            steps {
                sh '''
                    which python3 || sudo apt-get update && sudo apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/AnkitaJaiswal-git/amazon-fetch-order.git', branch: 'main'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
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

        stage('Fetch Orders from Amazon') {
            steps {
                sh 'python3 fetch_amazon_orders.py "$AMAZON_EMAIL" "$AMAZON_PASSWORD"'
            }
        }
    }
}
