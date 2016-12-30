function get_api_by_id(id){
    mykey  ="e9b783573b0f401d99c325696e95800b";
    cityid = id;
    url = "https://api.heweather.com/x3/weather?cityid="+cityid+"&key="+mykey;
    var xmlhttp=new XMLHttpRequest();
    xmlhttp.open("GET",url,false);
    xmlhttp.send();
    var tianqi  = document.getElementById("tianqi");
    var info = JSON.parse(xmlhttp.responseText);
    dinfo  = info["HeWeather data service 3.0"][0];
    return dinfo;
}

function get_api_by_ip(ip){
    mykey  ="e9b783573b0f401d99c325696e95800b";
    cityip = ip;
    url = "https://api.heweather.com/x3/weather?cityip="+cityip+"&key="+mykey;
    var xmlhttp=new XMLHttpRequest();
    xmlhttp.open("GET",url,false);
    xmlhttp.send();
    var tianqi  = document.getElementById("tianqi");
    var info = JSON.parse(xmlhttp.responseText);
    dinfo  = info["HeWeather data service 3.0"][0];
    return dinfo;
}

function get_api_by_cityname(name){
    mykey  ="e9b783573b0f401d99c325696e95800b";
    cityname = name;
    url = "https://api.heweather.com/x3/weather?city="+cityname+"&key="+mykey;
    var xmlhttp=new XMLHttpRequest();
    xmlhttp.open("GET",url,false);
    xmlhttp.send();
    var tianqi  = document.getElementById("tianqi");
    var info = JSON.parse(xmlhttp.responseText);
    dinfo  = info["HeWeather data service 3.0"][0];
    return dinfo;
}

function showinfo(info){
    //info  = get_api_by_id("CN101200105");
    //css下雨样式，未启用。
    //if(parseInt(info.now.cond.code)<=313&&parseInt(info.now.cond.code)>=300){
    //    document.getElementById("tianqi").className="weather rain";
    //}else{
    //    document.getElementById("tianqi").className="";
    //}
    var cond = document.getElementById("condimg");
    cond.src="http://files.heweather.com/cond_icon/"+ info.now.cond.code+".png";

    //document.getElementById("tianqi").style.background="url("+cond.src+") no-repeat ";

    var city = document.getElementById("city");
    city.innerHTML=info.basic.city;

    var time = document.getElementById("time");
    time.innerHTML=info.basic.update.loc;

    var tmp = document.getElementById("tmp");
    tmp.innerHTML=info.now.tmp;

    var cw_brf = document.getElementById("cw_brf");
    cw_brf.innerHTML=info.suggestion.cw.brf;

    var cw_txt = document.getElementById("cw_txt");
    cw_txt.innerHTML=info.suggestion.cw.txt;

    var uv_brf = document.getElementById("uv_brf");
    uv_brf.innerHTML=info.suggestion.uv.brf;

    var uv_txt = document.getElementById("uv_txt");
    uv_txt.innerHTML=info.suggestion.uv.txt;

    var drsg_brf = document.getElementById("drsg_brf");
    drsg_brf.innerHTML=info.suggestion.drsg.brf;

    var drsg_txt = document.getElementById("drsg_txt");
    drsg_txt.innerHTML=info.suggestion.drsg.txt;

    var qlty = document.getElementById("qlty");
    aqi = info.aqi.city.aqi;

    qlty.innerHTML=aqitest(aqi);
    for (var i =0;i<7;i++){
        var dayimg = document.getElementById("day"+i+"img");
        var daytxt = document.getElementById("day"+i+"txt");
        dayimg.src= "http://files.heweather.com/cond_icon/"+ info.daily_forecast[i].cond.code_d+".png";
        dayimg.alt= info.daily_forecast[i].cond.txt_d;
        daytxt.innerHTML= info.daily_forecast[i].cond.txt_d;
    }
    daily_forcast(info);
}

function changecity(){
    var cityname =  document.getElementById("cityname").value;
    info  = get_api_by_cityname(cityname);
    showinfo(info) ;

}
function aqitest(aqi){
    if(aqi>=0&&aqi<=50) t = "<span style='color: #00e400'>优<span>";
    if(aqi>=51&&aqi<=100) t ="<span style='color: #ff0'>良<span>";
    if(aqi>=101&&aqi<=150) t ="<span style='color: #ff7e00'>轻度污染<span>";
    if(aqi>=151&&aqi<=200) t ="<span style='color: #f00'>中度污染<span>";
    if(aqi>=201&&aqi<=300) t ="<span style='color: #99004c'>重度污染<span>";
    if(aqi>300) t ="<span style='color: #7e0023'>严重污染<span>";
    return t;
}

function daily_forcast(info){
    var myChart = echarts.init(document.getElementById('daily_forecast'));

    var option = {
        title: {
            text: '         未来天气'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:['最高温度','最低温度']
        },

        xAxis: {
            data: [info.daily_forecast[0].date.slice(5),info.daily_forecast[1].date.slice(5),info.daily_forecast[2].date.slice(5),info.daily_forecast[3].date.slice(5),info.daily_forecast[4].date.slice(5),info.daily_forecast[5].date.slice(5),info.daily_forecast[6].date.slice(5)]
        },
        yAxis: {},
        series: [{
            name: '最高温度',
            type: 'line',
            smooth: true,
            data: [info.daily_forecast[0].tmp.max,info.daily_forecast[1].tmp.max, info.daily_forecast[2].tmp.max, info.daily_forecast[3].tmp.max,info.daily_forecast[4].tmp.max,info.daily_forecast[5].tmp.max,info.daily_forecast[6].tmp.max]
        },
            {
                name: '最低温度',
                type: 'line',
                smooth: true,
                data: [info.daily_forecast[0].tmp.min,info.daily_forecast[1].tmp.min, info.daily_forecast[2].tmp.min, info.daily_forecast[3].tmp.min,info.daily_forecast[4].tmp.min,info.daily_forecast[5].tmp.min,info.daily_forecast[6].tmp.min]
            }
        ]
    };
    myChart.setOption(option);
}

function main(){
    api = "http://restapi.amap.com/v3/ip?key=e440df74143d2e429531d1ebc7beac55";
    x = new XMLHttpRequest();
    x.open("GET",api,false);
    x.send();
    info  = JSON.parse(x.responseText);
    cityname = info.city.slice(0,-1);
    info  = get_api_by_cityname(cityname);
    //info  = get_api_by_ip("119.36.85.153");
    showinfo(info);
}

main();


function  is_enter(){
    var input = document.querySelector('input'),
        oldValue = '';

    input.addEventListener('keydown', function(e){
        oldValue = this.value;
    }, false);

    input.addEventListener('keyup', function(e){
        var code = e.keyCode;
        if( code == 13 ){
            changecity();
        }
    }, false);
}

is_enter();

var map = new AMap.Map('container',{
    zoom: 10,
    resizeEnable: true,
    center: [108.360237,36.175811]
});

map.setZoom(5);
//map.setCenter([108.360237,36.175811]);

map.on('click', function(e) {
    xy = e.lnglat.getLng()+","+e.lnglat.getLat(); //点击位置的坐标
    api  = "http://restapi.amap.com/v3/geocode/regeo?location="+xy+"&key=e440df74143d2e429531d1ebc7beac55";
    var fuck=new XMLHttpRequest();
    fuck.open("GET",api,false);
    fuck.send();
    city = JSON.parse(fuck.responseText);
    if(city.regeocode.addressComponent.city.length!=0){
        area = city.regeocode.addressComponent.city;
    } else{
        area = city.regeocode.addressComponent.province;
    }
     showinfo(get_api_by_cityname(area.slice(0,-1)));
    document.getElementById("cityname").value = area.slice(0,-1);
});