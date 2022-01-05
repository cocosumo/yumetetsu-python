def confirmationModal():
  return {
	"title": {
		"type": "plain_text",
		"text": "Modal Title"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"blocks": [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "title",
				"placeholder": {
					"type": "plain_text",
					"text": "What do you want to ask of the world?"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Title"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "multi_channels_select",
				"action_id": "channels",
				"placeholder": {
					"type": "plain_text",
					"text": "Where should the poll be sent?"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Channel(s)"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "option_1",
				"placeholder": {
					"type": "plain_text",
					"text": "First option"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Option 1"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "option_2",
				"placeholder": {
					"type": "plain_text",
					"text": "How many options do they need, really?"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Option 2"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"action_id": "add_option",
					"text": {
						"type": "plain_text",
						"text": "Add another option  "
					}
				}
			]
		}
	],
	"type": "modal"
  }