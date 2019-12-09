function Token() {
    $.ajax({
        url: 'http://localhost:8000/api/v2/login/',
        method: 'post',
        data: JSON.stringify({username: 'admin', password: 'admin'}),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response){localStorage.setItem('apiToken', response.token);},
        error: function (response, status) {
            console.log(response);
            console.log(status)
        }
    });
}


function projects(){
 $.ajax({
        url:"http://localhost:8000/api/v2/project/",
        method: "GET",
        dataType:"json",
        contentType:"application/json",
         success:function (response,status) {
            console.log(response);
            console.log(status);
        },
        error:function (error) {
            console.log(error)

        }
    })
}

function issue(){
 $.ajax({
        url:"http://localhost:8000/api/v2/issue/",
        method: "GET",
        dataType:"json",
        contentType:"application/json",
         success:function (response,status) {
            console.log(response);
            console.log(status);
        },
        error:function (error) {
            console.log(error)

        }
    })
}


function SelectionOfAllTasksOfaGivenProject(){
    $.ajax({
        url: 'http://localhost:8000/api/v2/project/3',
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        success:function (response,status) {
            console.log(response);
            console.log(status);
        },
        error:function (error) {
            console.log(error)

        }
    })


}


function RemoveIssue(){
    $.ajax({
        url: 'http://localhost:8000/api/v2/issue/26',
        method: 'delete',
        contentType: 'application/json',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        dataType: 'json',
        success:function (response,status) {
            console.log(response);
            console.log(status);
        },
        error:function (error) {
            console.log(error)

        }
    })

}

function CreatIssue(){
     $.ajax({
        url: 'http://localhost:8000/api/v2/issue/',
        method: 'POST',
        contentType: 'application/json',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        data: JSON.stringify({summary: 'rthvcdfvh', description: 'cvbccbgbc', status: 17, type: 7, project: 7, created_by: 1, assigned_to: null}),
        dataType: 'json',
         success:function (response,status) {
            console.log(response);
            console.log(status);
        },
        error:function (error) {
            console.log(error)

        }

    })

}


$(document).ready(function () {
    projects();
    issue();
    SelectionOfAllTasksOfaGivenProject();
    RemoveIssue();
    CreatIssue();
    Token()
})




