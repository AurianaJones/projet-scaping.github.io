//chart function
function chart(options, data) {
	
  //appearance options

  var cOptions = {
    chart: {
      renderTo: options.renderTo,
      backgroundColor: {
        linearGradient: [0, 0, 500, 500],
        stops: [
          [0, 'green'],
          [1, 'rgb(240, 240, 255)']
        ]
      },
      borderWidth: 2,
      plotBackgroundColor: 'red',
      plotShadow: true,
      plotBorderWidth: 1,
      type: options.cType,
      style: { fontFamily: options.font }
    }
    ,
      title: {
          text: options.cTitle
      },
  
      xAxis: {
          categories: options.categories
      },
      yAxis: {
          title: {
              text: options.yTitle
          }
      },
  
  plotOptions: {
    column: {
      stacking: options.stack,
        dataLabels: {
        enabled: true,
        color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white'
      }
    }, 
    bar: {
      stacking: options.stack,
      dataLabels: {
        enabled: true,
        color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white'
      }
    },
    area: {
      stacking: 'normal',
      lineColor: '#666666',
      lineWidth: 1,
      marker: {
        lineWidth: 1,
        lineColor: '#666666'
      }
    },
    pie: {
      allowPointSelect: true,
      cursor: 'pointer',
      dataLabels: {
        enabled: true,
        format: '<b>{point.name}</b>: {point.percentage:.1f} %',
        style: {
          color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
        }
      }
    }

  },
  series: data
  };
 var chart = new Highcharts.Chart(cOptions);
}
