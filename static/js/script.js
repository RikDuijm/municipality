$(document).ready(function () {

    $(function() {
    $('#datetimepicker1').datetimepicker({
        format: 'L, LT',
        date: moment()
        });
    });

});

/* code used from: https://jsfiddle.net/taditdash/hDtA3/ */
function AvoidSpace(event) {
    var k = event ? event.which : window.event.keyCode;
    if (k == 32) return false;
}
