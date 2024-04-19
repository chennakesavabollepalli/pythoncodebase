pipeline {
  agent any 
  environment { 
    GIT_TAG = "${env.TAG_NAME}"
  }
  stages { 
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('POC') {
      steps {
        script {
          // def tagName = env.TAG_NAME
          if (env.TAG_NAME) {
              println "Prent Git tag:" env.TAG_NAME
          } else {
              println "This build was not having by a git tag"
          }

        
        }
      }
    }
  }


}
