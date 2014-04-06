set :layouts_dir, 'templates/layouts'

set :layout, 'default'
set :partials_dir, 'templates/partials'

set :css_dir, 'assets/css'
set :js_dir, 'assets/scripts'
set :images_dir, 'assets/images'
ignore 'assets/vendor/*'

with_layout false do
  page '*.atom'
  page '*.rss'
  page '*.xml'
  page '*.css'
end

activate :livereload

activate :blog do |blog|

end

Slim::Engine.set_default_options pretty: true, sort_attrs: true, shortcut: {'#' => {attr: 'id'}, '.' => {attr: 'class'}}

=begin

###
# Blog settings
###

# Time.zone = "UTC"

set :haml, { :attr_wrapper => '"' }

activate :blog do |blog|
  # This will add a prefix to all links, template references and source paths
  blog.prefix = "blog"

  blog.permalink = "{year}/{month}/{day}/{title}.html"
  # Matcher for blog source files
  blog.sources = "{title}.html"
  # blog.taglink = "tags/{tag}.html"
  blog.layout = "../templates/layouts/default"
  # blog.summary_separator = /(READMORE)/
  # blog.summary_length = 250
  # blog.year_link = "{year}.html"
  # blog.month_link = "{year}/{month}.html"
  # blog.day_link = "{year}/{month}/{day}.html"
  # blog.default_extension = ".markdown"

  blog.tag_template = "templates/tag.html"
  blog.calendar_template = "templates/calendar.html"

  # Enable pagination
  # blog.paginate = true
  # blog.per_page = 10
  # blog.page_link = "page/{num}"
end

page "/feed.xml", layout: false

###
# Compass
###

# Change Compass configuration
# compass_config do |config|
#   config.output_style = :compact
# end

###
# Page options, layouts, aliases and proxies
###

# Per-page layout changes:
#
# With no layout
# page "/path/to/file.html", layout: false
#
# With alternative layout
# page "/path/to/file.html", layout: :otherlayout
#
# A path which all have the same layout
# with_layout :admin do
#   page "/admin/*"
# end

# Proxy pages (http://middlemanapp.com/dynamic-pages/)
# proxy "/this-page-has-no-template.html", "/template-file.html", locals: {
#  which_fake_page: "Rendering a fake page with a local variable" }

###
# Helpers
###

# Automatic image dimensions on image_tag helper
# activate :automatic_image_sizes

# Reload the browser automatically whenever files change
activate :livereload

# Methods defined in the helpers block are available in templates
# helpers do
#   def some_helper
#     "Helping"
#   end
# end

set :layout, 'templates/layouts/default'

set :css_dir, 'assets/css'

set :js_dir, 'assets/scripts'

set :images_dir, 'assets/images'

# Build-specific configuration
configure :build do
  # For example, change the Compass output style for deployment
  # activate :minify_css

  # Minify Javascript on build
  # activate :minify_javascript

  # Enable cache buster
  # activate :asset_hash

  # Use relative URLs
  # activate :relative_assets

  # Or use a different image path
  # set :http_prefix, "/Content/images/"
end
=end