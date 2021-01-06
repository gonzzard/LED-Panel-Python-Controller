package com.example.myapplication;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothServerSocket;
import android.bluetooth.BluetoothSocket;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.graphics.Color;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;

import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Set;
import java.util.UUID;

public class MainActivity extends AppCompatActivity {

    private final String MAC_JETSON =  "4C:1D:96:FF:28:9A";
    private final String UUID_SERVICE = "00001101-0000-1000-8000-00805f9b34fb";

    private BluetoothAdapter mBluetoothAdapter;
    private OutputStream outputStream;
    private BluetoothSocket mBluetoothSocket;
    private BluetoothDevice jetsonNano;

    private Button btn_conectar;
    private Button btn_owo;
    private Button btn_voice;
    private Button btn_sleep;
    private Button btn_angry;
    private Button btn_sad;
    private Button btn_confused;
    private TextView cara_actual;

    @RequiresApi(api = Build.VERSION_CODES.R)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        cara_actual = findViewById(R.id.cara_actual);

        btn_conectar = findViewById(R.id.btn_conectar);
        btn_owo = findViewById(R.id.btn_owo);
        btn_voice = findViewById(R.id.btn_voice);
        btn_sleep = findViewById(R.id.btn_sleep);
        btn_angry = findViewById(R.id.btn_angry);
        btn_sad = findViewById(R.id.btn_sad);
        btn_confused = findViewById(R.id.btn_confused);

        btn_conectar.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                connect();
            }
        });
        btn_owo.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                connect();
                write("OWO");
            }
        });
        btn_voice.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                connect();
                write("VOICE");
            }
        });
        btn_sleep.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                connect();
                write("SLEEP");
            }
        });
        btn_angry.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                connect();
                write("ANGRY");
            }
        });
        btn_sad.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                connect();
                write("SAD");
            }
        });
        btn_confused.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                connect();
                write("CONFUSED");
            }
        });
    }

    @Override
    protected void onPause() {
        super.onPause();
        try {
            mBluetoothSocket.close();
            btn_conectar.setText("Reconectar");
            btn_conectar.setBackgroundColor(Color.RED);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void onStop() {
        super.onStop();
        try {
            mBluetoothSocket.close();
            btn_conectar.setText("Reconectar");
            btn_conectar.setBackgroundColor(Color.RED);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        connect();
    }

    public void write(String s){
        try {
            outputStream.write(s.getBytes());
            outputStream.flush();
            cara_actual.setText(s);
            Log.d("JETSON", "MENSAJE ENVIADO A JETSON NANO");
        } catch (IOException e) {
            Log.e("JETSON", "ERROR AL ENVIAR MENSAJE A JETSON NANO");
        }
    }

    public void connect() {
        if (mBluetoothSocket == null || !mBluetoothSocket.isConnected())
        {
            try {
                mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
                jetsonNano = mBluetoothAdapter.getRemoteDevice(MAC_JETSON);
                mBluetoothSocket = jetsonNano.createRfcommSocketToServiceRecord(UUID.fromString(UUID_SERVICE));
                mBluetoothSocket.connect();
                outputStream = mBluetoothSocket.getOutputStream();
                btn_conectar.setText("Conectado");
                btn_conectar.setBackgroundColor(Color.GREEN);
                Log.d("JETSON", "CONEXION ESTABLECIDA CON JETSON NANO");
            } catch (IOException e) {
                btn_conectar.setText("Reconectar");
                btn_conectar.setBackgroundColor(Color.RED);
                Log.e("JETSON", "ERROR AL CONECTARSE CON JETSON NANO");
            }
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
    }
}