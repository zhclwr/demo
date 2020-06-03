// ==UserScript==
// @name         个人自用百度净化
// @namespace    http://zhclwr.xyz/
// @version      0.1
// @description  个人自用百度净化
// @author       Alex
// @include        *.baidu.com*
// @require      http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js
// @grant        GM_download
// @grant        GM_openInTab
// @grant        GM_setValue
// @grant        GM_getValue
// @grant        GM_xmlhttpRequest
// @grant        GM_addStyle
// @grant        unsafeWindow
// @grant        GM_getResourceURL
// @grant        GM_getResourceText
// ==/UserScript==

(function() {
    'use strict';
    $("#s_side_wrapper").hide()
    $("#bottom_layer").hide()
    $("#s_top_wrap").hide()
    $("#s_upfunc_menus").hide()
    $("#u_sp").hide()
    $(".rect").hide()
    $(".load-text").hide()

    let div1 = document.querySelector('.rect')
    div1.style.visibility = 'hidden'
    console.log(sMoreBar)
    let div2 = document.querySelector('.load-text')
    div2.style.visibility = 'hidden'

})();



