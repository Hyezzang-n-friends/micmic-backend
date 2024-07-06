node {
    stage('Clone repository') {
        git branch: 'main', credentialsId: 'github_access_token', url: 'https://github.com/Hyezzang-n-friends/micmic-backend.git'
    }

    stage('Build image') {
        script {
            dockerImage = docker.build("hyezzang/micmic-backend:v1.0")
        }
    }

    stage('Push image') {
        script {
            docker.withRegistry('', 'docker-access') {
                dockerImage.push()
            }
        }
    }
}
