
<template>
	<view>
		<uni-list>
			
				<uni-list-item title="灯光状态" note="当前灯光状态"
				
				 :rightText=lightstate>
				</uni-list-item>
				<uni-list-item title="空调状态" note="当前空调状态 "
				:rightText=airConditionerState />
			<uni-list-item title="门状态" clickable @click="onClick" note="当前门开关状态" 
			:rightText=illuminationIntensity />
			<uni-list-item title="温度" note="当前屋内温度 : 摄氏度"
			:rightText=tempNow />
			<uni-list-item title="湿度" note="当前屋内湿度 "
			:rightText=humidityNow />
			<uni-list-item :show-extra-icon="true"
			:show-switch="true" title="门开关" note="控制门开启或关闭" @switchChange="switchChange" :switch-checked="true"/>
			
			<uni-list-item title="返回登录页面" link="navigateTo" to="../index/index" @click="onClick" />
			


		</uni-list>
	</view>
</template>
<script>
	export default {
		components: {},
		data() {
			return {
				title:"data",
				lightstate: "close",
				illuminationIntensity: "100",
				tempNow :"24.5",
				humidityNow:"60",
				airConditionerState:"close",
				dataTemp : 0,
				initNow : 0,
			};
		},
		methods: {
			onClick(e){
				
			},
			switchChange(e) {
				if(this.dataTemp==0)
				{
					this.dataTemp=1
					this.illuminationIntensity = "close";
					this.client.publish('data',this.illuminationIntensity )
				}
				else
				{
					this.dataTemp=0
					this.illuminationIntensity = "open";
					this.client.publish('data',this.illuminationIntensity )
				}
				console.log(this.dataTemp)
				},
			sendAndChange(mqttClient){
				console.log(this.illuminationIntensity )
				mqttClient.publish('data',this.illuminationIntensity )
				
			},
			
			onShow() {
				var that = this;
				
				console.log("into mqtt")
				that.mqtt = require('mqtt/dist/mqtt.js')
				//#ifdef H5
				that.client = that.mqtt.connect('ws://192.168.43.227:8083/mqtt')
				// #endif
				// #ifdef MP-WEIXIN||APP-PLUS
				that.client = that.mqtt.connect('wx://192.168.43.227:8083/mqtt')
				//var client = mqtt.connect('wx://8.136.6.223:1883')
				// #endif
				that.client.on('connect', function() {
					//self.logs.push('on connect')
					that.client.subscribe('test_topic', function(err) {
						if (!err) {
							console.log("connect")
							that.client.publish('test_topic', 'app connect')
						}
					})
				}).on('reconnect', function() {
					
				}).on('error', function() {
					
				}).on('end', function() {
					
				}).on('message', function(topic, message) {
					console.log(topic)
					var strNow = message.toString()
					console.log(strNow)
					that.humidityNow = strNow.slice(0,2)
					that.tempNow = strNow.slice(2,4)
					var tNow = strNow.charAt(4)
					if(tNow == "1")
					{
						that.lightstate = "open"
					}
					else
					{
						that.lightstate = "close"
					}
					
					//that.sendAndChange(that.client);
					//console.log(page.data.illuminationIntensity )
					//client.publish('data',page.data.illuminationIntensity )
					//if(this.illuminationIntensity=="10")
					//{
					//	client.publish('data',"on" )
					//	console.log("on")
					//	
					//}
					//else
					//{
					//	client.publish('data',"off" )
					//	console.log("off")
					//}
					
				
				})
				
			}
		}
	};
</script> 
