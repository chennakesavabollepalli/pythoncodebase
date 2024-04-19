pipeline {
  agent any 
  environment { 
    GIT_TAG = "${env.TAG_NAME}"
  }
  stages { 
    stage('POC') {
      steps {
        script {
          sh """
            echo "${GIT_TAG}"
          """
        }
      }
    }
  }


}
