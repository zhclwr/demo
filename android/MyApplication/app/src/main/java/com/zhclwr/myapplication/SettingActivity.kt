package com.zhclwr.myapplication

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_setting.*

class SettingActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_setting)
        supportActionBar?.title = "地址设置"
        et_setting.setText("http://")
        bt_save.setOnClickListener {
            if ("" == et_setting.text.toString().trim() || "http://" == et_setting.text.toString().trim()) {
                Toast.makeText(this, "请正确输入地址", Toast.LENGTH_LONG).show()
            } else {
                val sp = getSharedPreferences("URL", Context.MODE_PRIVATE)
                sp.edit().putString("URL", et_setting.text.toString().trim()).commit()
                val intent = Intent()
                intent.setClass(this, MainActivity::class.java)
                setResult(1)
                finish()
            }
        }
    }
}