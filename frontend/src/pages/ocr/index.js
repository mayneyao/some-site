import React from 'react';
import Button from '@material-ui/core/Button';
import {withStyles} from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import axios from 'axios';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import LinearProgress from '@material-ui/core/LinearProgress';
import Grid from '@material-ui/core/Grid';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';

const styles = theme => ({
	button: {
		margin: theme.spacing.unit,
	},
	exitFullScreenButton: {
		margin: theme.spacing.unit,
		position: 'absolute',
		bottom: '1em',
		right: '1em'
	},
	input: {
		display: 'none',
	},
	app: {
		width: '100%',
		height: '100%'
	},
	sider: {
		maxHeight: '900px',
		overflowY: 'auto'
	}
});

class App extends React.Component {

	constructor(props) {
		super(props);
		let formData = new FormData();
		formData.append("lang", "krytan");
		formData.append("url", false);
		this.state = {
			lang: 'krytan',
			formData,
			url: undefined,
			res: undefined,
			showUrl: undefined,
			loading: false,
			boxesData: {}
		}
	}

	//清空所有画布
	clearAllCanvas = () => {
		let ctx1 = document.getElementById('select-font').getContext('2d');
		let ctx2 = document.getElementById('font-info').getContext('2d');
		let ctx3 = document.getElementById('background').getContext('2d');

		const {width, height} = this.state;
		ctx1.clearRect(0, 0, width, height);
		ctx2.clearRect(0, 0, width, height);
		ctx3.clearRect(0, 0, width, height);
	};

	// 绘制选中文字的方框
	drawSelectRect = (xy) => {
		const {width, height} = this.state;
		let canvas = document.getElementById('select-font');
		canvas.setAttribute('width', width);
		canvas.setAttribute('height', height);
		let ctx = canvas.getContext('2d');
		ctx.clearRect(0, 0, width, height);
		let [x1, y1, x2, y2] = xy.split('-');
		let x = parseInt(x1);
		let y = parseInt(y1);
		let iWidth = parseInt(x2) - x;
		let iHeight = parseInt(y2) - y;
		y = height - y - iWidth;
		ctx.strokeStyle = "blue";
		ctx.lineWidth = '2';
		ctx.strokeRect(x, y, iWidth, iHeight)
	};

	// 绘制所有识别文字的方框
	drawDataRect = (data) => {
		const {width, height} = this.state;
		let canvas = document.getElementById('font-info');
		canvas.setAttribute('width', width);
		canvas.setAttribute('height', height);
		let ctx = canvas.getContext('2d');
		Object.entries(data).map(item => {
			let [xy, val] = item;
			let [x1, y1, x2, y2] = xy.split('-');
			let x = parseInt(x1);
			let y = parseInt(y1);
			let iWidth = parseInt(x2) - x;
			let iHeight = parseInt(y2) - y;
			y = height - y - iHeight;
			ctx.strokeStyle = "red";
			ctx.lineWidth = '1';
			ctx.strokeRect(x, y, iWidth, iHeight)
		})

	};

	handleUrlChange = (e) => {
		let url = e.target.value;
		const {formData} = this.state;
		formData.set("url", url);
		this.setState({url})
	};

	handleUploadImage = (event) => {
		const file = event.target.files[0];
		console.log(file);
		let showUrl = URL.createObjectURL(file);
		let imgDom = new Image();
		imgDom.src = showUrl;
		imgDom.onload = () => {
			let canvas = document.getElementById('background');
			let ctx = canvas.getContext('2d');
			canvas.setAttribute('width', imgDom.width);
			canvas.setAttribute('height', imgDom.height);
			ctx.drawImage(imgDom, 0, 0);
			this.setState({
				width: imgDom.width,
				height: imgDom.height
			})
		};
		const {formData} = this.state;
		formData.append("image", file);
		this.setState({
			formData,
			showUrl
		});
	};

	handleLangChange = (e) => {
		let lang = e.target.value;
		const {formData} = this.state;
		formData.set("lang", lang);
		this.setState({
			formData,
			lang
		})
	};

	ocr = () => {
		const {formData} = this.state;
		this.setState({
			loading: true
		});
		axios.post('http://127.0.0.1:8000/ocr/api', formData, {
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		}).then(res => {
			this.setState({
				res: res.data.text,
				boxesData: res.data.boxes,
				loading: false
			});
			this.drawDataRect(res.data.boxes)
		})
	};

	handleItemClick = (xy) => {
		this.drawSelectRect(xy)
		console.log(xy)
	};

	exitApp = () => {
		let formData = new FormData();
		formData.append("lang", "krytan");
		formData.append("url", false);
		this.setState({
			lang: 'krytan',
			formData,
			url: undefined,
			res: undefined,
			showUrl: undefined,
			loading: false,
			boxesData: {}
		});
		this.clearAllCanvas();
	};

	render() {
		const {classes} = this.props;
		const {lang, url, res, showUrl, loading, boxesData} = this.state;
		const langMap = {
			krytan: '科瑞塔文',
			chi_sim: '中文简体',
			en: '英文'
		};
		return (
			<div className={classes.app}>
				<div>
					{loading && <LinearProgress/>}
					{
						!res && <div style={{paddingTop: '50px', textAlign: 'center'}}>
							{/*<Input*/}
							{/*placeholder="图片url"*/}
							{/*inputProps={{*/}
							{/*'aria-label': 'Description',*/}
							{/*}}*/}
							{/*value={url}*/}
							{/*onChange={this.handleUrlChange}*/}
							{/*/>*/}
							<label htmlFor="lang">目标语言</label>
							<Select
								value={lang}
								onChange={this.handleLangChange}
								input={<Input name="lang" id="lang"/>}
							>
								{
									Object.entries(langMap).map(item => {
										let [val, name] = item;
										return <MenuItem value={val} key={val}>{name}</MenuItem>
									})
								}
							</Select>
							<input
								accept="image/*"
								className={classes.input}
								id="flat-button-file"
								multiple
								type="file"
								onChange={this.handleUploadImage}
							/>
							<label htmlFor="flat-button-file">
								<Button component="span" className={classes.button}>
									上传图片
								</Button>
							</label>
							<Button component="span" className={classes.button} onClick={this.ocr}>
								请求翻译
							</Button>
						</div>
					}
					<div>
						<Grid container>
							<Grid item xs={4} sm={4} md={4} className={classes.sider}>
								<List component="nav">
									{
										Object.entries(boxesData).map(item => {
											let [xy, val] = item;
											if (val !== '~') {
												return <ListItem key={xy} button
												                 onClick={() => this.handleItemClick(xy)}>
													<ListItemText primary={val}/>
												</ListItem>
											}
										})
									}
								</List>
							</Grid>
							<Grid item xs={4} sm={4} md={4}>
								<div style={{position: 'relative'}}>
									<canvas id="select-font" style={{zIndex: 3, position: "absolute"}}/>
									<canvas id="font-info" style={{zIndex: 2, position: "absolute"}}/>
									<canvas id="background" style={{zIndex: 1, position: "absolute"}}/>
								</div>
							</Grid>
							<Grid item xs={4} sm={4} md={4}>
								{res}
							</Grid>
						</Grid>
					</div>
					{
						res && <Button variant="fab" aria-label="Delete" className={classes.exitFullScreenButton}
						               onClick={this.exitApp}>
							<ExitToAppIcon/>
						</Button>
					}
				</div>
			</div>
		);
	}
}

export default withStyles(styles)(App);