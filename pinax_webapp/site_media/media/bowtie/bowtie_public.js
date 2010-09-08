

var x = 150, y = 150;
var dx = 2, dy = 4;
var WIDTH, HEIGHT, ctx;
var canvas,cur_pos,sec_pos,ir;
var count = 15000;
var clear_after=1000*60*5;

var last_pos=[];
var userdivs = {};
var userids = {};
var usernames = {};
var user_list = [];

var sprite_keys=[
't_amg1_lf1.gif','t_isd1_lf1.gif','t_mst1_lf1.gif','t_spd1_lf1.gif','t_ybo1_lf1.gif',
't_avt1_lf1.gif','t_jli1_lf1.gif','t_nja1_lf1.gif','t_syb1_lf1.gif','t_ygr1_lf1.gif',
't_bmg1_lf1.gif','t_kin1_lf1.gif','t_npc1_lf1.gif','t_thf1_lf1.gif','t_zph1_lf1.gif',
't_chr1_lf1.gif','t_knt1_lf1.gif','t_pdn1_lf1.gif','t_trk1_lf1.gif',
't_dvl1_lf1.gif','t_man1_lf1.gif','t_scr1_lf1.gif','t_wmg1_lf1.gif',
't_ftr1_lf1.gif','t_mnt1_lf1.gif','t_skl1_lf1.gif','t_wmn1_lf1.gif',
't_gsd1_lf1.gif','t_mnv1_lf1.gif','t_smr1_lf1.gif','t_wnv1_lf1.gif'
];

var valid_z="2";

last_update = {};


var mapholder = $('#mapholder');

// place(1,'t_s.png',1,10)

function init() {
  init_search();
  load_users();
  load_positions();
  return setInterval(load_positions, count);	
}

function init_search() {
  $('#search').hover( function () { $(this).addClass("hover"); },
        function () { $(this).removeClass("hover"); }
     );
  $('#search').click( function() { $('#badge_search').show().focus().select(); });
  
  $('#badge_search').keyup(function() {
     click_id($(this).val());
     
  });
  $('#badge_search').change(function() {
     click_id($(this).val());
  });
  $('#badge_search').blur(function() {
     $(this).hide();
  });
}

function click_id(uid) {
   uid_int = parseInt(uid);
   if (uid_int != uid) {
       // text, not numeric
       uid=usernames[uid];
       if (!uid) {
          $('#badge_search').css('background-color','rgb(255,192,192)'); // red
          return;
       }
   }
   udiv=userdivs[uid];
   if (udiv) {
      mapholder.find('.uimg').removeClass('clicked');
      udiv.addClass("clicked");
      $('#badge_search').css('background-color','rgb(192,255,192)'); // green
   } else if ((uid >= 1000) && (uid <= 9999)) {
      $('#badge_search').css('background-color','rgb(255,192,192)'); // red
   } else if (uid.toString().length > 4) {
      $('#badge_search').css('background-color','rgb(255,192,192)'); // red
   } else {
      $('#badge_search').css('background-color','white');
   }
}

function load_positions() {
    $.getJSON("http://api.hope.net/api/location/?jsoncallback=?",
              function(data){
                  if (data) {
                     cur_pos = data;
                     redraw(data);
                  }
              });
    
}

function load_users() {
   $.getJSON("http://api.hope.net/api/users/?jsoncallback=?",
            function(data) {
                  if(data) {
                       var userid,username;
                       for (i in data) {
                           userid = data[i][0];
                           username = data[i][1].username;
                           var udiv=userdivs[userid];
                           console.log("updating userid "+userid);
                           if (udiv) {
                              update_tooltip(userid,div);
                           }
                           userids[userid] = username;
                           usernames[username] = userid;
                       }
                       user_list=data;
                  }
            }
   );
}

function clear_old() {
   var now = (new Date()).getTime();
   for (var i in last_update) {
      if (last_update[i] > 0 && (now-last_update[i]) > clear_after) {
         userdivs[i].fadeOut(1000);
         last_update[i]=0;
      }
   }
}

function update_tooltip(uid,udiv) {
   var img=sprite_keys[uid%sprite_keys.length];
   uimg = $('<img src="/site_media/media/bowtie/lgs/'+img+'" height="16" width="16">');
   var tooltip_text;
   if (userids[uid]) {
      tooltip_text = userids[uid] + "(" + uid + ")";
   } else {
      tooltip_text = uid;
   }

   utooltip = $('<div class="tooltip">'+tooltip_text+'</div>');
   udiv.empty();
   udiv.append(uimg);
   udiv.append(utooltip);
}

function place(uid,x,y) {
   last_update[uid]=(new Date()).getTime();
   var udiv;
   if (uid < 1) {
     // hacked badge
     return;
   }
   if (!mapholder.size()) {
      mapholder = $('#mapholder');
   }
   if (!userdivs[uid])  {
      udiv = $('<div class="uimg" id="ud'+uid+'"></div>');
      update_tooltip(uid,udiv);
      mapholder.append(udiv);
      udiv.css({top:scaley(y),left:scalex(x)},1000);
      userdivs[uid]=udiv;
      udiv.hover( function () { $(this).addClass("hover"); },
            function () { $(this).removeClass("hover"); }
      );
      udiv.click(function() {
            mapholder.find('.uimg').removeClass('clicked');
         if ($(this).hasClass("clicked")) {
            $(this).removeClass("clicked");
         } else {
            $(this).addClass("clicked");
         }
      });
   }
   udiv=userdivs[uid];
   if (x==0 && y==0) {
      if (udiv.filter(':visible').size()) {
         udiv.fadeOut();
      }
   } else {
      if (udiv.filter(':visible').size()==0) {
         udiv.css({top:scaley(y),left:scalex(x)});
         udiv.fadeIn();
      } else {
         udiv.animate({top:scaley(y),left:scalex(x)},1000);
      }
   }

}

function redraw(data) {
   for(var i=0;i<data.length;i++)
   {
      if (data[i].z==2) {
         place(data[i].user,data[i].x,data[i].y);
      }
   }
   clear_old();
}


function scale(x) {
    return 10*x + 20;
}

function scalex(x) {
    var sx=9*x + 30;
    if (sx > 680) {
       sx=700;
    }
    return sx;
}

function scaley(y) {
    var sy = 10*y+20;
    if (sy>670) {
       sy=670;
    }
    return sy;
}
