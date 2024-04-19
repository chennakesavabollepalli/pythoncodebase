pipeline {
  agent any 
  environment { 
    GIT_TAG = "${env.TAG_NAME}"
  }
  stages { 
    stage('POC') {
      steps {
        script {
          def tagName = env.TAG_NAME
          if (tagName) {
              println "Prent Git tag: ${tagName}"
          } else {
              println "This build was not having by a git tag"
          }

        
        }
      }
    }
  }


}
