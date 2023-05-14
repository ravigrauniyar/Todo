
function taskDetails(state, id) {

    var todoBody = document.getElementById('todo-body-'+id);
    var eyeCon = document.getElementById('eye-con-'+id);
    var hideCon = document.getElementById('hide-con-'+id);

    if (state === 'show') {
        todoBody.classList.add('slide-down');
        hideCon.classList.remove('hidden');
        eyeCon.classList.add('hidden');

    } else {
        todoBody.classList.remove('slide-down');
        hideCon.classList.add('hidden');
        eyeCon.classList.remove('hidden');
    }
}