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
                    sh "docker build -t ${env.DOCKER_IMAGE}:latest ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: 'https://index.docker.io/v1/']) {
                    sh "docker push ${env.DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                sh "docker run -d -p 5000:5000 ${env.DOCKER_IMAGE}:latest"
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed!"
        }
    }
}