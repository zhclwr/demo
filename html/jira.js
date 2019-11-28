// ==UserScript==
// @name         jira
// @namespace    http://zhclwr.net/
// @version      0.1
// @description  个人用的 jira 计时工具
// @author       Alex
// @include        *.xuetoutong.com*
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
    setTimeout(() => {
        let res = ""
        $(".sc-kpOJdX").each((index, item) => {
            let name = $(item).find('.sc-eHgmQL').find("a").text()
            let text = $(item).find('.sc-dxgOiQ').text()
            let hour = $(item).find('.sc-jWBwVP').text()
            res += `${index + 1}. ${name} ${text} ${hour} \n`
        })
        if(res) console.log(res)
    }, 2000)
})();



