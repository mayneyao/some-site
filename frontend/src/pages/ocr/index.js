import React from 'react';
import Button from '@material-ui/core/Button';
import {withStyles} from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import axios from 'axios';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';


const styles = theme => ({
	button: {
		margin: theme.spacing.unit,
	},
	input: {
		display: 'none',
	},
});

class App extends React.Component {

	constructor(props) {
		super(props);
		let formData = new FormData();
		formData.append("lang", "chi_sim");
		formData.append("url", false);
		this.state = {
			lang: 'chi_sim',
			formData,
			url: undefined,
			res: undefined,
			showUrl: undefined
		}
	}

	drawDataRect = (data) => {
		let ctx = document.getElementById('canvas').getContext('2d');
		const {width, height} = this.state;
		Object.entries(data).map(item => {
			let [xy, val] = item;
			let [x1, y1, x2, y2] = xy.split('-');
			let x = parseInt(x1);
			let y = parseInt(y1);
			let iwidth = parseInt(x2) - x;
			let iheight = parseInt(y2) - y;
			ctx.strokeStyle = "red";
			ctx.lineWidth = '1';
			ctx.strokeRect(x, y, iwidth, iheight)
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
			let canvas = document.getElementById('canvas');
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
		axios.post('http://127.0.0.1:8000/ocr/api', formData, {
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		}).then(res => {
			this.setState({
				res: res.data.text
			});
			this.drawDataRect(res.data.boxes)
		})
	};


	render() {
		const {classes} = this.props;
		const {lang, url, res, showUrl} = this.state;
		const langMap = {
			chi_sim: '中文简体',
			en: '英文'
		};
		return (
			<div className="App">
				<div style={{textAlign: 'center'}}>
					<div style={{paddingTop: 300}}>
						<Input
							placeholder="图片url"
							inputProps={{
								'aria-label': 'Description',
							}}
							value={url}
							onChange={this.handleUrlChange}
						/>
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
					</div>
					<div>
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
					</div>
					<Button component="span" className={classes.button} onClick={this.ocr}>
						请求翻译
					</Button>

					<div>
						<canvas id="canvas"></canvas>
					</div>
					{
						res
					}

				</div>

			</div>
		);
	}
}

export default withStyles(styles)(App);