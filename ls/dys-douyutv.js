!function(a){window.DYS=a}(function(){var a={},b=["property","install","uninstall","isPluginIn"],c={property:{loadtime:(new Date).getTime(),version:"2.0"},install:function(c,d){var e="[object Object]"==={}.toString.call(c);if(!e||!c.id&&!c.prop||void 0===c.handle)return!1;for(var f=c.prop||c.id,g=c.handle,h=0,i=b.length;i>h;h++)if(f===b[h])return!1;this[f]?d===!0&&(this[f]=g,a[f]++):(this[f]=g,a[f]=1)},uninstall:function(b){this.isPluginIn(b)&&(delete this[b],delete a[b])},isPluginIn:function(b){b=String(b);for(var c in a)if(b===String(c))return!0;return!1}};return c.install({id:"sence",handle:{}}),c}()),function(a){DYS.install({id:"field",handle:a})}(function(){var a=[],b=function(){return b.sence};return b.each=function(b){for(var c=a,d=0,e=c.length;e>d&&b(c[d],d)!==!1;d++);},b.filter=function(c){if(!c)return!1;if(!a||!a.length)return c;var d={};return b.each(function(a){var e=a.name,f=void 0===c[e]?b.defval(a.value):c[e];e=a.nick||e,d[e]=f}),d},b.format=function(a){if(!a)return!1;for(var c="[object Array]"==={}.toString.call(a)?a:[a],d=0,e=c.length;e>d;d++)c[d]=b.filter(c[d]);return c},b.config=function(c){c=c||{},c.sence&&(b.sence=c.sence),c.keys&&(a=c.keys)},b.defval=function(a){return"function"==typeof a?a():a},b}()),function(a){DYS.install({id:"point",handle:a})}(function(){var a=window.jQuery,b={join:".",max_count:4,elattr:{page:"data-page-point",point1:"data-point",point2:"data-point-2",point3:"data-point-3"}},c={property:b.elattr,make:function(){var c,d=[].slice.call(arguments);return c=1===d.length?a.isArray(d[0])?d[0].join(b.join):d[0]:d.join(b.join),this.format(c)},page:function(){var c,d,e=[a("body").attr(b.elattr.page)],f=[].slice.call(arguments);return 1===f.length?"[object Array]"===Object.prototype.toString.call(f[0])?c=e.concat(f[0]):(e.push(f[0]),c=e):c=e.concat(f),d=this.make(c)},pagep:function(){return a("body").attr(b.elattr.page)},area:function(c){var d,e=a(c).eq(0);return e.attr(b.elattr.point1)?d=this._area_1(c):e.attr(b.elattr.point2)?d=this._area_2(c):e.attr(b.elattr.point3)&&(d=this._area_3(c)),d},_area_1:function(c){var d=a(c).eq(0),e=d.attr(b.elattr.point1),f=this.page(e);return f},_area_2:function(c){var d=a(c).eq(0),e=d.attr(b.elattr.point2),f=d.closest("["+b.elattr.point1+"]").attr(b.elattr.point1)||0,g=this.page(f,e);return g},_area_3:function(c){var d=a(c).eq(0),e=d.attr(b.elattr.point3),f=d.closest("["+b.elattr.point2+"]").attr(b.elattr.point2)||0,g=d.closest("["+b.elattr.point1+"]").attr(b.elattr.point1)||0,h=this.page(g,f,e);return h},format:function(a){if(!a)return a;var c=a.split(b.join);if(c.length>b.max_count)return c.slice(0,b.max_count).join(b.join);if(c.length>=0&&c.length<b.max_count){for(var d=b.max_count-c.length,e=0;d>e;e++)c.push(0);return c.join(b.join)}return a}};return c}()),function(a){DYS.install({id:"submit",handle:a})}(function(){var a={suburl:"",subtype:{ajax:"ajax",form:"form",image:"image"},filter:null,IE7:navigator.appVersion.indexOf("MSIE 7.0")>0},b=function(c,d){var e=[].slice.call(arguments);if(!a.suburl||!e.length)return!1;1===e.length&&(d=c,c=null),c?c.type=c.type||a.subtype.ajax:c=c||{type:a.subtype.ajax,queue:!1};var f=String(c.type).toLowerCase(),g=!!c.queue;if(!$.isFunction(a.filter)||a.filter(c,d)!==!1)if(g)DYS.queue.may(d);else{var h=b["_by_"+f];if("function"==typeof h)return h(d)}};return b.config=function(b){b=b||{},b.suburl&&(a.suburl=b.suburl),$.isFunction(b.filter)&&(a.filter=b.filter)},b._data_15=function(a){return{multi:JSON.stringify(a),v:"1.5"}},b._by_ajax=function(c){var d=a.suburl,e=DYS.field.format(c),f=b._data_15(e);return a.IE7?$.ajax(d,{type:"post",dataType:"jsonp",data:f}):$.post(d,f)},b._by_form=function(a){},b._by_image=function(a){},b}()),function(a){DYS.install({id:"queue",handle:a.create()})}(function(){var a=function(a){this.init(a)};return a.prototype.init=function(a){a=a||{},this._config={cache:a.cache||[],size:a.size||5},this.may()},a.prototype.release=function(){DYS.submit(this._config.cache),this._config.cache=[]},a.prototype.may=function(){var a=[].slice.call(arguments);if(a.length>1&&(this._config.cache=this._config.cache.concat(a)),1===a.length){var b=a[0],c={}.toString.call(b);"[object Array]"===c?this._config.cache=this._config.cache.concat(b):this._config.cache.push(b)}this._config.cache.length>=this._config.size&&this.release()},a.prototype.config=function(a){a=a||{},"number"==typeof a.size&&a.size>=0&&(this._config.size=a.size)},a.create=function(b){return new a(b)},a}()),function(a){DYS.install({id:"cache",handle:a})}(function(){var a={},b={next:function(b){var c=(new Date).getTime(),d=b||{};return a[c]=d,c},set:function(b,c){a[b]=c},get:function(b){return a[b]},remove:function(b){var c={};for(var d in a)b!==d&&(c[d]=a[d]);a=c},clear:function(){a={}}};return b}()),function(a){DYS.install({id:"storage",handle:a})}(function(){var a={cookie_pre:"_dys_",page_refer_cookie:"page_refer3",page_refer_max_count:10},b={set:function(b,c,d,e,f){b=a.cookie_pre+b,f=f?"; path="+f:"",e=e?";domain="+e:"";var g=new Date;g.setTime(g.getTime()+24*d*60*60*1e3);var h="expires="+g.toUTCString();document.cookie=b+"="+c+"; "+h+f+e},get:function(b,c){b=(c||a.cookie_pre)+b+"=";for(var d=document.cookie.split(";"),e=0;e<d.length;e++){for(var f=d[e];" "==f.charAt(0);)f=f.substring(1);if(-1!=f.indexOf(b))return f.substring(b.length,f.length)}return""},list:function(){for(var b=document.cookie.split(";"),c=[],d=0;d<b.length;d++){for(var e=b[d];" "==e.charAt(0);)e=e.substring(1);if(-1!=e.indexOf(a.cookie_pre)){var f=e.split("="),g=f[0],h=f[1];g&&(g=g.replace(a.cookie_pre,"")),c.push({key:g,value:h})}}return c},remove:function(a,b){this.set(a,"",-1,b)},clear:function(){for(var a=this.list(),b=0,c=a.length;c>b;b++)this.remove(a[b].key)}},c={save:function(a,c,d){var e=location.host.split("."),f="";e=e.slice(e.length-2),e.unshift(""),f=e.join("."),b.set(a,c,d||1,f,"/")},get:function(a,c){return b.get(a,c)},remove:function(a,c){b.remove(a,"/")},clear:function(){b.clear()}};return c.ext={page:{refer:function(){var b,d,e=a.page_refer_cookie,f=a.page_refer_max_count,g=[].slice.call(arguments);return"clear"===g[0]?c.remove(a.page_refer_cookie):(b=c.get(e),b=b?b.split("."):[],g.length?(d={}.toString.call(g[0]),b="[object Array]"===d?b.concat(g[0]):b.concat(g),b.length>f&&(b=b.slice(b.length-f)),b=b.join("."),void c.save(e,b)):b.join("."))}}},setTimeout(function(){b.remove("page_refer"),b.remove("page_refer2")},100),c}()),function(a){DYS.install({id:"trigger",handle:a})}(function(){var a=window.jQuery,b={dom_data_attr:"dysdomdata",dom_extdata_attr:"dysdomextdata",data_point_key:"point",data_other_key:"other",trigger_type:{domready:"domready",dompoint:"dompoint",linkrefer:"linkrefer",hot:"hot",heart:"heart"}},c=function(a){var d=[].slice.call(arguments,1);if(a===b.trigger_type.domready)c.domready.apply(this,d);else if(a===b.trigger_type.dompoint)c.dompoint.apply(this,d);else if(a===b.trigger_type.linkrefer)c.linkrefer.apply(this,d);else if(a===b.trigger_type.hot)c.hot.apply(this,d);else if(a===b.trigger_type.heart)return c.heart.apply(this,d)};return c.config=function(a){a=a||{},a.dataPointKey&&(b.data_point_key=a.dataPointKey),a.dataOtherKey&&(b.data_other_key=a.dataOtherKey)},c.IS={linkInvalid:function(a){return!a||"#"===a||0===a.indexOf("javascript:")},stopDYSEvent:function(a){return a.originalEvent?a.originalEvent.stopDYSEvent===!0:a.stopDYSEvent===!0}},c.stopDYSEvent=function(a){a.originalEvent?a.originalEvent.stopDYSEvent=!0:a.stopDYSEvent=!0},c.domready=function(c){a(function(){var d=DYS.point.page(),e=DYS.storage.ext.page.refer(),f={};if(f[b.data_other_key]={},location.search.indexOf("from")>=0){for(var g,h=location.search.replace("?","").split("&"),i=0,j=h.length;j>i;i++)if(h[i].indexOf("from")>=0){g=h[i].split("=")[1];break}g&&(f[b.data_other_key].fr=g)}e&&e.length&&(f[b.data_other_key].refer=e),d&&(f[b.data_point_key]=d,f=a.extend(!0,{},f,c),DYS.submit(f))})},c.dompoint=function(){var d=DYS.point.property,e="["+d.point1+"]",f="["+d.point2+"]",g="["+d.point3+"]",h=[e,f,g];a.each(h,function(d,e){var f=a(e),g=f.not("a"),h=f.find("a");g=g.filter(function(){return!a(this).data(b.dom_data_attr)}),h=h.filter(function(){return!a(this).data(b.dom_data_attr)}),g.length&&c.dompoint._com(g),h.length&&c.dompoint._link(h)})},c.dompoint._com=function(d){var e=a(d);e.each(function(){var c=a(this),d=DYS.point.area(this),e={};e[b.data_point_key]=d,c.data(b.dom_data_attr,e)}),e.on("click",function(d){if(!c.IS.stopDYSEvent(d)){c.stopDYSEvent(d);var e=a(this).data(b.dom_data_attr);DYS.queue.may(e)}})},c.dompoint._link=function(d){var e=a(d);e.each(function(){var d=a(this),e=d.attr("href"),f=DYS.point.area(this),g={},h=null;g[b.data_point_key]=f,c.IS.linkInvalid(e)||(h=DYS.point.pagep()),d.data(b.dom_data_attr,g),h&&d.data(b.dom_extdata_attr,h)}),e.on("mousedown",function(d){if(!c.IS.stopDYSEvent(d)){c.stopDYSEvent(d);var e=a(this),f=e.data(b.dom_data_attr),g=e.data(b.dom_extdata_attr);DYS.submit(f),g&&DYS.storage.ext.page.refer(g)}}),e.on("click",function(a){c.stopDYSEvent(a)})},c.linkrefer=function(d){var e=DYS.point.property,f="["+e.point1+"]",g="["+e.point2+"]",h="["+e.point3+"]",i=[f,g,h],j=d?a(d).find("a"):a("a");a.each(i,function(a,b){j=j.not(b)}),j.length&&(j.each(function(){var d=a(this),e=d.attr("href"),f=null;c.IS.linkInvalid(e)||(f=DYS.point.pagep()),f&&d.data(b.dom_extdata_attr,f)}),j.on("mousedown",function(d){if(!c.IS.stopDYSEvent(d)){c.stopDYSEvent(d);var e=a(this),f=e.data(b.dom_extdata_attr);f&&DYS.storage.ext.page.refer(f)}}),j.on("click",function(a){c.stopDYSEvent(a)}))},c.hot=function(a){return!1},c.hot.center=function(b,d){var e=a(b?b:document),f=null;e.on("mousedown",function(b){a(b.target).is("a")?c.hot.centerHandle(b,e,d):(clearTimeout(f),f=setTimeout(function(){c.hot.centerHandle(b,e,d)},200))})},c.hot.centerHandle=function(b,c,d){var e=b.pageY,f=b.pageX,g=c.width(),h=c.height(),i=a(b.target).closest(d.exclude),j=[],k=[];a(b.toElement).is("html,body")||(i.size()>0&&(e=b.offsetY+i.position().top),f=parseInt(f-g/2),j.push(f),j.push(e),k.push(g),k.push(h),DYS.submit({point_id:DYS.point.page(),ext:{ishot:1,pos:j.join(","),wh:k.join(","),htype:0}}))},c.hot.left=function(b,d){var e=a(b?b:document),f=null;e.on("mousedown",function(b){a(b.target).is("a")?c.hot.leftHandle(b,e,d):(clearTimeout(f),f=setTimeout(function(){c.hot.leftHandle(b,e,d)},200))})},c.hot.leftHandle=function(b,c,d){var e=b.pageY,f=b.pageX,g=c.width(),h=c.height(),i=a(b.target).closest(d.exclude),j=[],k=[];if(!a(b.toElement).is("html,body")){i.size()>0&&(e=b.offsetY+i.position().top);var l=Number.prototype.toFixed;j.push(l.call(f/g*100,1)),j.push(l.call(e/h*100,1)),k.push(g),k.push(h),DYS.submit({point_id:DYS.point.page(),ext:{ishot:1,pos:j.join(","),wh:k.join(","),htype:1}})}},c.heart=function(){DYS.submit({point_id:"h.1.0.0"})},c}()),function(a){DYS.field.config({sence:"douyutv",keys:[{name:"url",nick:"u",value:location.href},{name:"point_id",nick:"p",value:""},{name:"did",nick:"d",value:function(){return DYS.storage.get("did",$SYS.cookie_pre)||""}},{name:"uid",nick:"i",value:function(){return DYS.storage.get("uid",$SYS.cookie_pre)||0}},{name:"rid",nick:"rid",value:function(){return window.$ROOM&&$ROOM.room_id?$ROOM.room_id:""}},{name:"page_t",nick:"pt",value:function(){return parseInt(DYS.property.loadtime/1e3,10)}},{name:"occur_t",nick:"ot",value:function(){return parseInt((new Date).getTime()/1e3,10)}},{name:"ext",nick:"e",value:""},{name:"device",nick:"a",value:"web"},{name:"version",nick:"v",value:""},{name:"refer",nick:"r",value:document.referrer},{name:"fp",nick:"fp",value:""}]}),DYS.trigger.config({dataPointKey:"point_id",dataOtherKey:"ext"}),DYS.submit.config({suburl:window.$SYS?$SYS.fh||"":""}),DYS.sence.douyutv={first:function(){DYS.trigger("heart")},init:function(){DYS.trigger("domready",{ext:{domready:1,ua:navigator.userAgent,pageurl:location.href}}),DYS.trigger("dompoint"),DYS.trigger("linkrefer")},loadready:function(){var a=DYS.point.page();a&&DYS.submit({point_id:a,ext:{loadready:1}})}},DYS.sence.douyutv.first(),a(DYS.sence.douyutv.init)}(window.jQuery);