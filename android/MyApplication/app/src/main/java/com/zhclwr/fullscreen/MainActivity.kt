package com.zhclwr.fullscreen

import android.app.ProgressDialog
import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.os.Bundle
import android.view.MenuItem
import android.view.WindowManager
import android.webkit.CookieManager
import android.webkit.CookieSyncManager
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.GravityCompat
import com.google.android.material.navigation.NavigationView
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.app_bar_main.*
import kotlinx.android.synthetic.main.content_main.*

class MainActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener {

    lateinit var dialog: ProgressDialog
    lateinit var sp: SharedPreferences
    var url = "http://49.234.151.237:9528/"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        // 右下fab 点击开启 Drawer
        fab.setOnClickListener {
            drawer_layout.openDrawer(GravityCompat.START)
        }
        //
        sp = getSharedPreferences("URL", Context.MODE_PRIVATE)
        val u = sp.getString("URL", "")
        if (u != "") {
            url = u
        }
        // 隐藏 ActionBar
        supportActionBar?.hide()
        // 全屏显示
        window.setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN)
        // Drawer 点击事件  在 最下面的 onNavigationItemSelected
        nav_view.setNavigationItemSelectedListener(this)
        // 允许javaScript执行
        web_view.settings.javaScriptEnabled = true
        // 显示等待弹窗
        dialog = ProgressDialog.show(this, "正在加载，请稍后", null)
        // webview监听
        web_view.webViewClient = object : WebViewClient(){
//            @RequiresApi(Build.VERSION_CODES.LOLLIPOP)
//            override fun shouldOverrideUrlLoading(view: WebView?, request: WebResourceRequest?): Boolean {
//                view?.loadUrl(request?.url.toString())
//                return false
//            }
//
//            override fun shouldOverrideUrlLoading(view: WebView?, url: String?): Boolean {
//                view?.loadUrl(url)
//                return false
//            }

            override fun onPageFinished(view: WebView?, url: String?) {
                super.onPageFinished(view, url)
                if(dialog.isShowing) {
                    // 加载完 隐藏弹窗
                    dialog.dismiss()
                }

            }

        }
        // 加载页面
        web_view.loadUrl(url)
        val imageView = findViewById<ImageView>(R.id.imageView)
//        imageView.setOnLongClickListener {
//
//            val intent = Intent()
//            intent.setClass(this, SettingActivity::class.java)
//            startActivity(intent)
//            true
//        }

    }
    // 监听返回键
    override fun onBackPressed() {
        if (drawer_layout.isDrawerOpen(GravityCompat.START)) {
            drawer_layout.closeDrawer(GravityCompat.START)
        } else {
            super.onBackPressed()
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if (requestCode == 1 && resultCode ==1) {
            val u = sp.getString("URL", "")
            if (u != "") {
                url = u
            }
            web_view.clearCache(false)
            val cookieSyncManager = CookieSyncManager.createInstance(web_view.getContext())
            val cookieManager = CookieManager.getInstance()
            cookieManager.setAcceptCookie(true)
            cookieManager.removeSessionCookie()
            cookieManager.removeAllCookie()
            cookieSyncManager.sync()
            web_view.loadUrl(url)
            dialog.show()
        }
        super.onActivityResult(requestCode, resultCode, data)
    }

    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.nav_home -> {
                web_view.loadUrl(url)
                dialog.show()
            }
            R.id.nav_logout -> {
                web_view.clearCache(false)
                val cookieSyncManager = CookieSyncManager.createInstance(web_view.getContext())
                val cookieManager = CookieManager.getInstance()
                cookieManager.setAcceptCookie(true)
                cookieManager.removeSessionCookie()
                cookieManager.removeAllCookie()
                cookieSyncManager.sync()
                web_view.loadUrl(url)
                dialog.show()
            }
            R.id.nav_setting -> {
                val intent = Intent()
                intent.setClass(this, SettingActivity::class.java)
                startActivityForResult(intent, 1)
            }

        }
        drawer_layout.closeDrawer(GravityCompat.START)
        return true
    }
}
