node{
    stage('Clone repository'){
        git credentialsId: "github_access_token", url: "https://github.com/Hera-Moon/micmic-.git"
    }

    stage('Build image'){
        dockerImage = docker.build("hyezzang/micmic-backend:v1.0")
    }
    stage('Push image'){
        withDockerRegistry([ credentialsId: "docker-access", url: ""]){
        dockerImage.push()
        }
    }
}