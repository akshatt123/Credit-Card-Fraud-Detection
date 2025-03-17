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
        stage('Checkout Repository') {
    steps {
        script {
            echo '🔄 Checking out repository...'
            checkout([
                $class: 'GitSCM',
                branches: [[name: '*/main']],
                doGenerateSubmoduleConfigurations: false,
                extensions: [[$class: 'WipeWorkspace']],
                userRemoteConfigs: [[
                    url: "${REPO_URL}",
                    credentialsId: 'github-credential'
                ]]
            ])
            echo '✅ Repository checked out successfully.'
        }
    }
}

        stage('Install Dependencies') {
            steps {
                script {
                    try {
                        echo '📦 Installing dependencies...'
                        bat 'pip install --no-cache-dir -r requirements.txt'
                        echo '✅ Dependencies installed successfully.'
                    } catch (Exception e) {
                        echo "❌ Dependency installation failed: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping pipeline due to dependency installation failure.")
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        echo '🧪 Running tests...'
                        bat 'python -m pytest tests/ --maxfail=1 --disable-warnings'
                        echo '✅ Tests executed successfully.'
                    } catch (Exception e) {
                        echo "❌ Tests failed: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping pipeline due to test failure.")
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    try {
                        echo '🔍 Running SonarQube analysis...'
                        withSonarQubeEnv("${SONARQUBE_SERVER}") {
                            bat 'sonar-scanner -Dsonar.projectKey=fraud-detection -Dsonar.sources=.'
                        }
                        echo '✅ SonarQube analysis completed.'
                    } catch (Exception e) {
                        echo "⚠️ SonarQube analysis failed: ${e}"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        echo '🐳 Building Docker image...'
                        bat "docker build --no-cache -t ${DOCKER_IMAGE}:latest ."
                        echo '✅ Docker image built successfully.'
                    } catch (Exception e) {
                        echo "❌ Docker build failed: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping pipeline due to Docker build failure.")
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    try {
                        echo '📤 Pushing Docker image to Docker Hub...'
                        withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                            bat "docker push ${DOCKER_IMAGE}:latest"
                        }
                        echo '✅ Docker image pushed successfully.'
                    } catch (Exception e) {
                        echo "❌ Docker push failed: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping pipeline due to Docker push failure.")
                    }
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    try {
                        echo '🚀 Deploying application with Docker Compose...'
                        bat "docker-compose down"  // Stop existing containers
                        bat "docker-compose up --build -d"  // Build & start new containers
                        echo '✅ Application deployed successfully.'
                    } catch (Exception e) {
                        echo "❌ Deployment failed: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping pipeline due to deployment failure.")
                    }
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully! 🎉'
        }
        failure {
            echo '❌ Pipeline failed. Please check logs and fix errors. 🔍'
        }
    }
}
