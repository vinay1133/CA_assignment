// frappe.pages['overview'].on_page_load = function(wrapper){
// 	new OverviewPage(wrapper)
// }
// //page content
// OverviewPage = Class.extend({
// 	init: function(wrapper){
// 		this.page = frappe.ui.make_app_page({
// 			parent: wrapper,
// 			title: 'Progress overview',
// 			single_column: true
// 		});
// 		this.make()
// 	},

// 	make: function(){
// 		var me = this;	
// 		$(frappe.render_template('home', {'name': 'Ishaan'})).appendTo(this.page.main);
// 		// Attaching event handler for the button
// 		$(this.page.main).on('click', '#alertButton', () => {
// 			alert('Button clicked!');
// 	});
// 	}
// })


frappe.pages['overview'].on_page_load = function(wrapper){
	let page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Progress overview',
		single_column: true
	});

	let buttonBlock = $(frappe.render_template('filters'));

	// Function to render 'home' template
	function renderHomeTemplate(env) {
			$(frappe.render_template('home', env)).appendTo(page.main);
	}

	// Bind click event to the button
	buttonBlock.find('#fetch').on('click', function() {
			$(page.main).empty();

			frappe.call({
				method: 'bytenba.analytics.page.overview.overview.getData',
				args: {
				},
				callback: function(response) {
						if (response) {
							renderHomeTemplate();
						}
				}
		});
		
	});

	// Append button block before the main block
	buttonBlock.insertBefore(page.main);

	// Initial rendering of 'home' template
	renderHomeTemplate();
}	

// OverviewPage = Class.extend({
// 	init: function(wrapper){
// 		this.page = frappe.ui.make_app_page({
// 			parent: wrapper,
// 			title: 'Progress overview',
// 			single_column: true
// 		});
// 		this.make()
// 	},

// 	make: function(){
// 		var me = this;	
// 		$(frappe.render_template('home', {'name': 'Ishaan'})).appendTo(this.page.main);
// 		// Attaching event handler for the button
// 		$(this.page.main).on('click', '#alertButton', () => {
// 			alert('Button clicked!');
// 	});
// 	}
// })

