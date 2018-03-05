$(document).ready(function () {

    Vue.filter('formatDate', function (value) {
        if (value) {
            return moment(String(value)).format('MM/DD/YYYY-HH:mm')
        }
    });


    Vue.component('line-chart', {
        extends: VueChartJs.Line,
        props: ['data', 'options'],
        mounted: function () {
            this.renderChart(this.data, this.options)
        }

    });


});