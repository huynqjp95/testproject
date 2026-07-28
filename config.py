from point import *

COMBOS = {
   "target" : [
        {"action" : "target", "x":BUTTON_TARGET[0],"y":BUTTON_TARGET[1],"delay":5},
   ],

   "changeRange20" : [
        {"action" : "tap", "x":BUTTON_SETTING[0],"y":BUTTON_SETTING[1],"delay":0.2},
        {"action" : "tap", "x":RANGE20[0],"y":RANGE20[1],"delay":0.2},
        {"action" : "tap", "x":BUTTON_BAGACH[0],"y":BUTTON_BAGACH[1],"delay":0.2},
   ],
   "changeRange50" : [
        {"action" : "tap", "x":BUTTON_SETTING[0],"y":BUTTON_SETTING[1],"delay":0.2},
        {"action" : "tap", "x":RANGE50[0],"y":RANGE50[1],"delay":0.2},
        {"action" : "tap", "x":BUTTON_BAGACH[0],"y":BUTTON_BAGACH[1],"delay":0.2},
   ],
   "changeRange100" : [
        {"action" : "tap", "x":BUTTON_SETTING[0],"y":BUTTON_SETTING[1],"delay":0.2},
        {"action" : "tap", "x":RANGE100[0],"y":RANGE100[1],"delay":0.2},
        {"action" : "tap", "x":BUTTON_BAGACH[0],"y":BUTTON_BAGACH[1],"delay":0.2},
   ],
   "changeRange200" : [
        {"action" : "tap", "x":BUTTON_SETTING[0],"y":BUTTON_SETTING[1],"delay":0.2},
        {"action" : "tap", "x":RANGE200[0],"y":RANGE200[1],"delay":0.2},
        {"action" : "tap", "x":BUTTON_BAGACH[0],"y":BUTTON_BAGACH[1],"delay":0.2},
   ],
   "boss" : [
        {"action" : "tap", "x":BUTTON_BAGACH[0],"y":BUTTON_BAGACH[1],"delay":0.5},
        {"action" : "tap", "x":BUTTON_ACTIVITY[0],"y":BUTTON_ACTIVITY[1],"delay":0.5},
        {"action" : "tap", "x":BUTTON_BOSS[0],"y":BUTTON_BOSS[1],"delay":0.5},
        {"action" : "tap", "x":BUTTON_CHALLENGE[0],"y":BUTTON_CHALLENGE[1],"delay":0.5},
        {"action" : "tap", "x":BUTTON_GROUPOUT[0],"y":BUTTON_GROUPOUT[1],"delay":0.5}
   ],

     "outBoss":[
          {"action" : "tap", "x":X_OUT_BOSS[0],"y":X_OUT_BOSS[1],"delay":0.5},
          {"action" : "tap", "x":MAIN_CITY[0],"y":MAIN_CITY[1],"delay":0.5}
     ],

     "outGame":[
          {"action" : "tap", "x":BUTTON_BAGACH[0],"y":BUTTON_BAGACH[1],"delay":0.5},
          {"action" : "tap", "x":SETTING[0],"y":SETTING[1],"delay":0.5},
          {"action" : "tap", "x":SETTING[0],"y":SETTING[1],"delay":0.5}
     ],

     "goCoordinates":[
          {"action" : "tap", "x":SPEED_BOOT[0],"y":SPEED_BOOT[1],"delay":0.5},
          {"action" : "tap", "x":CHAT_BOX[0],"y":CHAT_BOX[1],"delay":0.5},
          {"action" : "tap", "x":BUTTON_PRIVATE[0],"y":BUTTON_PRIVATE[1],"delay":0.5},
          {"action" : "tap", "x":COMEBACK_CHAT[0],"y":COMEBACK_CHAT[1],"delay":0.5},
          {"action" : "tap", "x":NAME_PRIVATE[0],"y":NAME_PRIVATE[1],"delay":0.5},
          {"action" : "tap", "x":COORDINATES[0],"y":COORDINATES[1],"delay":0.5}
     ],

     "inGameGoCoord":[
          {"action" : "tap", "x":BUTTON_ENTERGAME[0],"y":BUTTON_ENTERGAME[1],"delay":5},
          {"action" : "tap", "x":SPEED_BOOT[0],"y":SPEED_BOOT[1],"delay":0.5},
          {"action" : "tap", "x":CHAT_BOX[0],"y":CHAT_BOX[1],"delay":0.5},
          {"action" : "tap", "x":BUTTON_PRIVATE[0],"y":BUTTON_PRIVATE[1],"delay":0.5},
          {"action" : "tap", "x":COMEBACK_CHAT[0],"y":COMEBACK_CHAT[1],"delay":0.5},
          {"action" : "tap", "x":NAME_PRIVATE[0],"y":NAME_PRIVATE[1],"delay":0.5},
          {"action" : "tap", "x":COORDINATES[0],"y":COORDINATES[1],"delay":0.5}
     ],
     
     "pickupbox1":[
          {"action" : "tap", "x":BUTTON_BAGACH[0],"y":BUTTON_BAGACH[1],"delay":0.5},
          {"action" : "tap", "x":COLLECT[0],"y":COLLECT[1],"delay":0.5},
          {"action" : "tap", "x":EXPLORE[0],"y":EXPLORE[1],"delay":0.5},
          {"action" : "tap", "x":BOX_1[0],"y":BOX_1[1],"delay":0.5},
          {"action" : "tap", "x":RECEIVING[0],"y":RECEIVING[1],"delay":0.5},
          {"action" : "tap", "x":RECEIVING[0],"y":RECEIVING[1],"delay":0.5},
          {"action" : "tap", "x":CHARACTER[0],"y":CHARACTER[1],"delay":0.5},
          {"action" : "tap", "x":CHARACTER[0],"y":CHARACTER[1],"delay":0.5},
          {"action" : "tap", "x":CHARACTER[0],"y":CHARACTER[1],"delay":0.5}
     ],
     "pickupbox2":[
          {"action" : "tap", "x":BUTTON_BAGACH[0],"y":BUTTON_BAGACH[1],"delay":0.5},
          {"action" : "tap", "x":COLLECT[0],"y":COLLECT[1],"delay":0.5},
          {"action" : "tap", "x":EXPLORE[0],"y":EXPLORE[1],"delay":0.5},
          {"action" : "tap", "x":BOX_2[0],"y":BOX_2[1],"delay":0.5},
          {"action" : "tap", "x":RECEIVING[0],"y":RECEIVING[1],"delay":0.5},
          {"action" : "tap", "x":RECEIVING[0],"y":RECEIVING[1],"delay":0.5},
          {"action" : "tap", "x":CHARACTER[0],"y":CHARACTER[1],"delay":0.5},
          {"action" : "tap", "x":CHARACTER[0],"y":CHARACTER[1],"delay":0.5},
          {"action" : "tap", "x":CHARACTER[0],"y":CHARACTER[1],"delay":0.5}
     ],
     "pickupbox3":[
          {"action" : "tap", "x":BUTTON_BAGACH[0],"y":BUTTON_BAGACH[1],"delay":0.5},
          {"action" : "tap", "x":COLLECT[0],"y":COLLECT[1],"delay":0.5},
          {"action" : "tap", "x":EXPLORE[0],"y":EXPLORE[1],"delay":0.5},
          {"action" : "tap", "x":BOX_3[0],"y":BOX_3[1],"delay":0.5},
          {"action" : "tap", "x":RECEIVING[0],"y":RECEIVING[1],"delay":0.5},
          {"action" : "tap", "x":RECEIVING[0],"y":RECEIVING[1],"delay":0.5},
          {"action" : "tap", "x":CHARACTER[0],"y":CHARACTER[1],"delay":0.5},
          {"action" : "tap", "x":CHARACTER[0],"y":CHARACTER[1],"delay":0.5},
          {"action" : "tap", "x":CHARACTER[0],"y":CHARACTER[1],"delay":0.5}
     ],
   "login":[
          {"action" : "tap", "x":ICON_GAME[0],"y":ICON_GAME[1],"delay":40},
          {"action" : "tap", "x":BUTTON_TARGET[0],"y":BUTTON_TARGET[1],"delay":1},
          {"action" : "tap", "x":BUTTON_CHAT[0],"y":BUTTON_CHAT[1],"delay":5},
          {"action" : "tap", "x":BUTTON_ENTERGAME[0],"y":BUTTON_ENTERGAME[1],"delay":0.5}
   ]
}

JOBS = {
     "device_id" : {
     "21:29" : "changeRange200",
     "21:30" : "boss",
     "21:40":"outBoss",
     "21:41":"outGame"
}
}