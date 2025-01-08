all category xpath = "//a[@data-toggle='dropdown']/ancestor::ul[@class='navbar-nav all-categories-dropdown']"

p.categoyr
//a[@data-toggle='dropdown']/ancestor::ul[@class='navbar-nav all-categories-dropdown']//div[@title='Warehouse Deals']



p.category ---> child. cat xpath.....
//a[@data-toggle='dropdown']/ancestor::ul[@class='navbar-nav all-categories-dropdown']//div[@title='Warehouse Deals']/ancestor::div[@class='row no-gutters']/div[@class='col scl-content']//span[text()='Toys']

p.cat ---- child.cat --- following sibling links
for example... warehouse cat--->

//a[@data-toggle='dropdown']/ancestor::ul[@class='navbar-nav all-categories-dropdown']//div[@title='Warehouse Deals']/ancestor::div[@class='row no-gutters']/div[@class='col scl-content']//span[text()='Automotive Equipments-Parts']



-- ADD to wishlist locator on PLPage::

// div[text() = 'Genuine Apple magic keyboard  for Mac A2450 - Soft Pink'] / ancestor::div[@class ='product-card style2ProductCard listing-products'] // button[@ title='Add to wishlist']

--- Account hover
//a[@class='topbar-link dropdown-toggle']

--first account hover then click on wishlist
//a[@class='topbar-link dropdown-toggle']/ancestor::div[@class='topbar-text dropdown disable-autohide']//div/a[@href='https://www.cartlow.com/user/wishlist']
