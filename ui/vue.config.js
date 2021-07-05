module.exports = {
	devServer: {
		proxy: {
		    '^/api': {
                target: 'http://restapi:8000/',
            },
            '^/admin': {
                target: 'http://restapi:8000/',
            },
            '^/static':{
                target: 'http://restapi:8000/',
            }
		}
	}
}
