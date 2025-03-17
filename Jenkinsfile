pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/akshatt123/Credit-Card-Fraud-Detection.git'
        DOCKER_IMAGE = 'akshatt123/fraud-detection'
        SONARQUBE_SERVER = 'SonarQube'
        CONTAINER_NAME = 'fraud-detection-app'
        DB_CONTAINER_NAME = 'fraud-detection-db'
        DATABASE_URL = 'postgresql://postgres:password@fraud-detection-db:5432/fraud_db'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    sh 'sonar-scanner -Dsonar.projectKey=fraud-detection -Dsonar.sources=.'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:latest ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh "docker-compose down"  // Stop existing containers
                sh "docker-compose up --build -d"  // Build & start new containers
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check logs.'
        }
    }
}
