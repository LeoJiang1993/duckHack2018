$(document).ready(function () {
    var editor = CKEDITOR.replace('editor', {});

    $("input[name=submit]").click(function () {
        $('textarea[name=content]').html(editor.getData());
        $.post('/idea/save',
            $('#newsEditor').serialize(), function (text) {
                alert('Succeed');
                $('html').html(text);
            }
        );
    });


});
