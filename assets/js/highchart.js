Highcharts.chart('container', {
    chart: {
        type: 'spline',
        backgroundColor: '#ffa500',
        animation: Highcharts.svg, // don't animate in old IE
        marginRight: 10,
        events: {
            load: function () {
            function between(min, max) {  
                return Math.floor(
                  Math.random() * (max - min) + min
                )
              }

                // set up the updating of the chart each second
                var series = this.series[0];
                setInterval(function () {
                    var x = (new Date()).getTime(), // current time
                        y = between(230, 910);
                    series.addPoint([x, y], true, true);
                }, 1000);
            }
        }
    },

    time: {
        useUTC: false
    },

    title: {
        style: {
    			color: '#ffffff',
                fontFamily: 'Poppins'
    		},
        text: 'Hasil Tangkapan Ikan Tongkol'
    },

    accessibility: {
        announceNewData: {
            enabled: true,
            minAnnounceInterval: 15000,
            announcementFormatter: function (allSeries, newSeries, newPoint) {
                if (newPoint) {
                    return 'New point added. Value: ' + newPoint.y;
                }
                return false;
            }
        }
    },

    xAxis: {
    		title: {
            text: 'Waktu',
            style: {
              color: '#ffffff',
              fontFamily: 'Poppins'
            },
        },
        type: 'datetime',
        tickPixelInterval: 150
    },

    yAxis: {
        title: {
            text: 'Berat (gr)',
            style: {
              color: '#ffffff',
              fontFamily: 'Poppins'
            },
        },
        plotLines: [{
            value: 0,
            width: 1,
            color: '#ffffff'
        }]
    },

    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x:%Y-%m-%d %H:%M:%S}<br/>{point.y:.2f}'
    },

    legend: {
        enabled: false
    },

    exporting: {
        enabled: false
    },

    series: [{
        name: 'Hasil Tangkapan Ikan Tongkol',
        color: '#02507e',
        data: (function () {
        function between(min, max) {  
          return Math.floor(
            Math.random() * (max - min) + min)
        }
            // generate an array of random data
            var data = [],
                time = (new Date()).getTime(),
                i;

            for (i = -19; i <= 0; i += 1) {
                data.push({
                    x: time + i * 1000,
                    y: between(230, 910)
                });
            }
            return data;
        }())
    }]
});

Highcharts.chart('container2', {
    chart: {
        type: 'spline',
        backgroundColor: '#ffa500',
        animation: Highcharts.svg, // don't animate in old IE
        marginRight: 10,
        events: {
            load: function () {
            function between(min, max) {  
                return Math.floor(
                  Math.random() * (max - min) + min
                )
              }

                // set up the updating of the chart each second
                var series = this.series[0];
                setInterval(function () {
                    var x = (new Date()).getTime(), // current time
                        y = between(300, 1500);
                    series.addPoint([x, y], true, true);
                }, 1000);
            }
        }
    },

    time: {
        useUTC: false
    },

    title: {
        style: {
    			color: '#ffffff',
          fontFamily: 'Poppins'
    		},
        text: 'Hasil Tangkapan Ikan Cakalang'
    },

    accessibility: {
        announceNewData: {
            enabled: true,
            minAnnounceInterval: 15000,
            announcementFormatter: function (allSeries, newSeries, newPoint) {
                if (newPoint) {
                    return 'New point added. Value: ' + newPoint.y;
                }
                return false;
            }
        }
    },

    xAxis: {
    		title: {
            text: 'Waktu',
            style: {
              color: '#ffffff',
              fontFamily: 'Poppins'
            },
        },
        type: 'datetime',
        tickPixelInterval: 150
    },

    yAxis: {
        title: {
            text: 'Berat (gr)',
            style: {
              color: '#ffffff',
              fontFamily: 'Poppins'
            },
        },
        plotLines: [{
            value: 0,
            width: 1,
            color: '#ffffff'
        }]
    },

    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x:%Y-%m-%d %H:%M:%S}<br/>{point.y:.2f}'
    },

    legend: {
        enabled: false
    },

    exporting: {
        enabled: false
    },

    series: [{
        name: 'Hasil Tangkapan Ikan Cakalang',
        color: '#02507e',
        data: (function () {
        function between(min, max) {  
          return Math.floor(
            Math.random() * (max - min) + min)
        }
            // generate an array of random data
            var data = [],
                time = (new Date()).getTime(),
                i;

            for (i = -19; i <= 0; i += 1) {
                data.push({
                    x: time + i * 1000,
                    y: between(300, 1500)
                });
            }
            return data;
        }())
    }]
});

Highcharts.chart('container3', {
    chart: {
        backgroundColor: '#ffa500',
        type: 'column'
    },
    title: {
    		style: {
    					color: '#ffffff',
          		fontFamily: 'Poppins'
    				},
        text: 'Hasil Tangkapan Ikan Tongkol dan Cakalang'
    },
    xAxis: {
        categories: [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'Mei',
            'Jun',
            'Jul',
            'Ag',
            'Sep',
            'Okt',
            'Nov',
            'Des'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
        		style: {
    					color: '#ffffff',
          		fontFamily: 'Poppins'
    				},
            text: 'Jumlah Tangkapan (ton)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} ton</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: [{
    		color: '#ffffff',
        name: 'Tongkol',
        data: [0.1770, 0.0758, 0.2678, 0.1605, 0.1290, 2.1623, 0.5610, 0.4493, 3.1845, 2.7465, 0.1935, 0.8933]

    }, {
    		color: '#02507e',
        name: 'Cakalang',
        data: [2.8777, 3.9388, 3.5467, 4.5998, 4.3663, 3.8798, 4.7680, 5.1233, 4.6788, 4.0085, 3.7877, 4.0450]

    }]
});