
<template>
	<view>
		<uni-list>

		<uni-list-item :show-extra-icon="true"  
		:show-switch="true" title="灯光开关" note="控制灯光" @switchChange="switchChange" :switch-checked="true"/>
			<uni-list-item :show-extra-icon="true"
			:show-switch="true" title="门开关" note="控制门开关" @switchChange="switchChange" :switch-checked="true"/>
			<uni-list-item :show-extra-icon="true"
			:show-switch="true" title="加湿开关" note="控制加湿器" @switchChange="switchChange" :switch-checked="true"/>
			
			<uni-list-item title="空调控制页面" link="navigateTo" to="../airControler/airControler" @click="onClick" />


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
			};
		},
		methods: {
			switchChange(e) {
				},
			onClick(e) {
				this.illuminationIntensity = "133",
				uni.showToast({
					title: 'clicked'
				});
				
			}
		}
	};
</script>
