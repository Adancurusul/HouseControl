<template>
	<view class="content">
		
		<!-- <view class="login_img"><image mode="aspectFill" src="/static/image/iamhe.png"></image></view> -->
		
		<view class="login_from">
			
			<view class="login_from_input">
				<view class="login_from_name">手机号</view>
				<view class="login_from_fun"><input type="text" placeholder="请输入手机号码"></view>
			</view>

			<view class="login_from_input">
				<view class="login_from_name">密码</view>
				<view class="login_from_fun"><input type="digit" v-model="login.password" @input="onKeyUserPwInput" password="true" placeholder="请输入登录密码"></view>
			</view>

			<view class="login_from_input">
				<view class="login_from_name">验证码</view>
				<view class="login_from_fun">
					<input style="width: 40%; text-align: left" type="digit" maxlength="6" placeholder="验证码">
					<text class="getyzm" v-if="yzmbotshou"  @click="getyzm">获取验证码</text>
					<text class="getyzm" style="color: #888;" v-if="yzmbothide">{{times}}秒后重新获取</text>
				</view>
			</view>

			<view class="login_from_input">
				<view class="login_from_name">用户名</view>
				<view class="login_from_fun">
					<input type="text" v-model="login.userName" @input="onKeyUserNameInput" placeholder="请输入用户名">
					<label class="cuIcon-scan cuicon"></label>
				</view>
			</view>
			
			
			<view class="login_from_dl">
				<button @click="denglu">注册</button>
			</view>
			
			<view class="logo_xieyi">
				<label @click="moutcl" :class="gouxSta?'cuIcon-squarecheckfill':'cuIcon-square'"></label>
				<view class="logo_text"></text></view>
			</view>
			
		</view>
		
	</view>
</template>
<script>
	
	



   export default {

   data(){
     return {
		//value3: [],
		//label3: '',
		//list1: areaData,
		login: {
			userName: "",
			password: "",
		},
		gouxSta:false,
		times:60,
		yzmbotshou:true,
		yzmbothide:false
		 
	}
	   },
    methods: {
		onKeyUserNameInput: function(event) {
			this.userName = event.target.value
		},
		onKeyUserPwInput: function(event) {
			this.password = event.target.value
		},
		moutcl(){
			if( this.gouxSta == false){
				this.gouxSta = true
			}else{
				this.gouxSta = false
			}
		},
		onHide() {
			this.client.end(true);
			console.log("hidePage")
		
		},
		denglu(){
			this.client.publish('login_topic', this.login.userName + "," + this.login.password)
			if( this.gouxSta == false){
				//uni.navigateTo({
				//    url: '../index'  
				//});
				uni.navigateBack({
					delta: 1
				});
								
			}else{
				uni.showToast({
					"title":"账号不存在",
					"icon":'none'
				})
			}		
		},
		
		onLoad() {
			var self = this
			//self.logs.push('connect')
			self.mqtt = require('mqtt/dist/mqtt.js')
			// #ifdef H5
			self.client = self.mqtt.connect('ws://192.168.43.227:8083/mqtt')
			// #endif
			// #ifdef MP-WEIXIN||APP-PLUS
			self.client = self.mqtt.connect('wx://192.168.43.227:8083/mqtt')
			// #endif
			self.client.on('connect', function() {
				//self.logs.push('on connect')
				self.client.subscribe('test_topic', function(err) {
					if (!err) {
						self.client.publish('test_topic', 'app connect')
					}
				})
			}).on('reconnect', function() {
				//self.logs.push('on reconnect')
			}).on('error', function() {
				//self.logs.push('on error')
			}).on('end', function() {
				//self.logs.push('on end')
			}).on('message', function(topic, message) {
				console.log(message)
				//self.logs.push(message.toString())
			})
		},
		getyzm(){
				var num = 60;
				this.yzmbotshou = false,
				this.yzmbothide = true
				var interval = setInterval(() =>{
					 if(this.is_sendsms == false){this.sendsms()}
					--this.times
				},1000)
				setTimeout(()=>{
					clearInterval(interval)
					this.yzmbotshou = true,
					this.yzmbothide = false,
					this.times = num
				},60000)			
		},
		
		handleTap(picker) {
			this.$refs[picker].show()
		},
		handleChange(e) {
			console.log('change::', e)
		},
		handleConfirm(e) {
			// 如果存在多个picker，可以在picker上设置dataset属性，confirm中获取，就能区分是哪个picker了
			console.log('confirm::', e)
			if (e) {
				const name = e.dataset.name
				const label = e.item.map(m => m.label).join('-')
				if (name && label) {
					this[name] = label
				}
			}
		},
		handleCancel(e) {
			console.log('cancel::', e)
		}	
		
		
		
     }
 }
</script>
<style>
	
	page{ background: #fff; }
	
	.login_img{ width: 100%; height: auto; margin-top: 90upx; }
	.login_img image{ width: 170upx; height: 170upx; display: block; margin: 0px auto; border-radius: 50%; }
	
	.login_from{ width: 100%; height: auto; box-sizing: border-box; padding: 20upx 8%; }
	
	.login_from_input{ width: 100%; height:auto; display: flex; flex-direction: row; justify-content: space-between; align-items: center; border-bottom: 1px #eee solid; padding: 40upx 0px; margin: 0px auto;  } 
	
	.login_from_name{ width: 20%; }
	.login_from_fun{ width: 80%; display: flex; flex-direction: row; justify-content: flex-end; align-items: center;  }
	.login_from_fun input{ width: 100%; text-align: left; font-size: 14px;  }
	
	
	.login_from_dl{ width: 100%; height: 50px; line-height: 50px; margin-top: 150upx;   }
	.login_from_dl button{ width: 100%; height: 50px; line-height: 50px; background: #00aaff; color: #fff; border-radius: 50px; }
	
	.logo_xieyi{ width: 100%; height: 40px; line-height: 40px; display: flex; flex-direction: row; margin-top: 30upx; align-items: center; color: #444; font-size: 14px; justify-content: center; }
	.logo_xieyi label{ font-size: 18px; margin-right: 1%; }
	
	.cuIcon-squarecheckfill{ color: #00aaff; }
	.logo_text text{ color: #00aaff; }
	
	.getyzm{ width: 60%; display: flex; flex-direction: row; justify-content: flex-end; color: #00aaff; }
	.cuicon{ font-size: 18px; }  
	
</style>

