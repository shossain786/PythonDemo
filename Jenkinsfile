pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-dockerhub-saddam/python-flask-app"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t ${env.DOCKER_IMAGE}:latest ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: 'https://index.docker.io/v1/']) {
                    bat "docker push ${env.DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                bat "docker run -d -p 5000:5000 ${env.DOCKER_IMAGE}:latest"
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed!"
        }
    }
}
