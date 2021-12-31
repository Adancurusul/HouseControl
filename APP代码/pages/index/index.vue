<template>
	<view class="contents">
		<view class="avatorWrapper">
			<view class="avator">
				<image class="img" src="../../static/logo.jpg" mode="widthFix"></image>
			</view>
		</view>
		<view class="form">
			<view class="inputWrapper">
				<input class="input" v-model="login.userName" @input="onKeyUserNameInput" type="text" value=""
					placeholder="请输入用户名" />
			</view>
			<view class="inputWrapper">
				<input class="input" v-model="login.password" @input="onKeyUserPwInput" type="password" value="" placeholder="请输入密码" />
			</view>
			<view>

				<button @click="loginBtn" class="loginBtn">
					<text>登录</text>
				</button>
			</view>
			<button @click="registerBtn" class="forgotBtn">
				<text>注册</text>
			</button>
			<button @click="connect" class="mqttBtn">
				<text>连接MQTT服务器</text>
			</button>
		</view>

		<view class="log">
			<view v-for="(log,index) in logs" class="" :key="index">
				{{log}}
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: 'Hello',
				logs: [],
				login: {
					userName: "",
					password: "",
				},
			}
		},
		methods: {
			onKeyUserNameInput: function(event) {
				this.userName = event.target.value
			},
			onKeyUserPwInput: function(event) {
				this.password = event.target.value
			},
			loginBtn() {
				this.client.publish('login_topic', this.login.userName + ";" + this.login.password)

				
				uni.showToast({
					title: this.userName
				})
			},
			registerBtn() {
				uni.navigateTo({
					url: '../register/register'
				});
				uni.showToast({
					title: "注册"
				})
			},
			onHide() {
				this.client.end(true);
				console.log("hidePage")

			},
			
			connect(){
				
			},
			onShow() {
				var self = this
				self.logs.push('connect')
				self.mqtt = require('mqtt/dist/mqtt.js')
				// #ifdef H5
				self.client = self.mqtt.connect('ws://192.168.43.227:8083/mqtt')
				// #endif
				// #ifdef MP-WEIXIN||APP-PLUS
				self.client = self.mqtt.connect('wx://192.168.43.227:8083/mqtt')
				// #endif
				self.client.on('connect', function() {
					self.logs.push('on connect')
					self.client.subscribe('test_topic', function(err) {
						if (!err) {
							self.client.publish('test_topic', 'app connect')
						}
					})
					self.client.subscribe('loginPass', function(err) {
						if (!err) {
							
						}
					})
				}).on('reconnect', function() {
					self.logs.push('on reconnect')
				}).on('error', function() {
					self.logs.push('on error')
				}).on('end', function() {
					self.logs.push('on end')
				}).on('message', function(topic, message) {
					
					var messageNow = message.toString()
					//self.logs.push(message.toString())
					console.log(messageNow)
					if(messageNow=="loginSuc")
					{
						uni.switchTab({
							url: '/pages/monitorPage/monitorPage'
						});
					}
					
					else if(messageNow == "loginFail")
					{
						uni.showToast({
							title: "error Login"
						})
					}
				})
			}
		}
	}
</script>

<style>
	.content {
		text-align: center;
		height: 400upx;
		word-break: break-all;
	}

	.contents {
		background: #00aaff;
		width: 100vw;
		height: 100vh;
	}

	.avatorWrapper {
		height: 30vh;
		width: 100vw;
		display: flex;
		justify-content: center;
		align-items: flex-end;
	}

	.avator {
		width: 200upx;
		height: 200upx;
		overflow: hidden;
	}

	.avator .img {
		width: 100%
	}

	.form {
		padding: 0 100upx;
		margin-top: 80px;
	}

	.inputWrapper {
		width: 100%;
		height: 80upx;
		background: white;
		border-radius: 20px;
		box-sizing: border-box;
		padding: 0 20px;
		margin-top: 25px;
	}

	.inputWrapper .input {
		width: 100%;
		height: 100%;
		text-align: center;
		font-size: 15px;
	}

	.loginBtn {
		width: 60%;
		height: 80upx;
		background: #77B307;
		border-radius: 50upx;
		margin-top: 50px;
		display: flex;
		justify-content: center;
		align-items: center;

	}

	.loginBtn .btnValue {
		color: white;
	}

	.forgotBtn {
		text-align: center;
		width: 40%;
		color: #EAF6F9;
		background: #00aaff;
		font-size: 15px;
		margin-top: 10px;
	}

	.mqttBtn {
		text-align: center;
		width: 80%;
		color: #EAF6F9;
		background: #00aaff;
		font-size: 15px;
		margin-top: 10px;
	}
</style>
