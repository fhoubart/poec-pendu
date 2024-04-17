pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Git clone'
                git 'https://github.com/fhoubart/poec-pendu.git'
            }
        }
        stage('Creation du manuel') {
            steps {
                echo 'Créaiton du manuel'
                bat 'type *.md > manual.md'
            }
        }
        stage('Creation du zip') {
            steps {
                echo 'Démarrage de la création du zip'
                bat 'tar -a -c -f pendu.zip pendu.py manual.md'
            }
            post {
                success {
                    archiveArtifacts artifacts: '*.zip,manual.md', followSymlinks: false
                }
            }
        }
    }
}
