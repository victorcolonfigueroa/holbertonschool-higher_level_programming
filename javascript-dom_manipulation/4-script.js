document.addEventListener("DOMContentLoaded", function() {
	document.querySelector("#add_item").addEventListener("click", function() {
		const newItem = document.createElement("li");
		newItem.textContent = "Item";
		document.querySelector("ul.my_list").appendChild(newItem);
	});
});