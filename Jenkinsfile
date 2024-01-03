def qa_stage_run=false


pipeline {

    agent any
    environment {
        SNYK_TOKEN = credentials('snyk-api-token')
    }
    stages {
        stage ('checkout') {
                    steps {
                        sh 'mkdir -p deployments'
                        dir("build")
                        {
                            git branch: "main",
                            credentialsId: "raj-epam",
                            url: 'https://github.com/raj-epam/appdeploydemo-fe.git'
                        }
                    }
                }

        //     }
        // }
    //stage ("Scan Code")
    //Docker Image Build
    stage ('Build') {
            steps {
                dir("build")
                {
                    sh 'docker build -t dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER} .'
                }
            }
        }
    stage('SYNK Scan') {
        steps {
            script{
                dir("build")
                    {
                        echo "Starting Scan"
                        def scanExitCode = sh(script: 'snyk container test dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER}  --file=./Dockerfile --json-file-output=vulnerabilities.json --org=raj-epam --project-name=python_demo-FE', returnStatus: true)
                        def junitXml = sh(script: 'python convert_to_junit.py < snyk-report.json', returnStdout: true).trim()
                        writeFile file: 'junit-results.xml', text: junitXml
                        junit skipPublishingChecks: true, allowEmptyResults :true, testResults: 'junit-results.xml'
                        echo "error code = ${scanExitCode}"
                    }
                }
            }
        }
        // stage ('Push') {
        //     steps {
        //         dir("build")
        //         {
        //             sh 'docker push dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER}'
        //         }
        //     }
        // }
    }
        post {
            // Clean after build
            always {
                cleanWs(cleanWhenNotBuilt: false,
                        deleteDirs: true,
                        disableDeferredWipeout: true,
                        notFailBuild: true,
                        patterns: [[pattern: '.gitignore', type: 'INCLUDE'],
                                [pattern: '.propsfile', type: 'EXCLUDE']])
            }
    }


}