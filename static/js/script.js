$(document).ready(function () {
    /* set the date and time no right now */
    $(function() {
    $('#datetimepicker1').datetimepicker({
        format: 'L, LT',
        date: moment()
        });
    });

});

/* code used from: https://jsfiddle.net/taditdash/hDtA3/ to restrict use of spaces in username upon registering*/
function AvoidSpace(event) {
    var k = event ? event.which : window.event.keyCode;
    if (k == 32) return false;
}
