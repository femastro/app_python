function sendData(){
    var nota = document.getElementById('nota')
    var formulario = document.getElementById('formulario').value
    nota.innerHTML='<div class="alert alert-success alert-dismissible fade show" role="alert">Iniciando Proceso Espere !!!......</div>'
    formulario.submit()

}