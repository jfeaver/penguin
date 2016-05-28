module Penguin
  module Helpers
    module SchemaTagHelper
      def author_tag(author, options = {})
        options.merge!({
          itemprop: :author,
          itemscope: true,
          itemtype: 'http://schema.org/Person'
        })
        name_tag = content_tag(:span, author, itemprop: :name)
        content_tag(:span, name_tag, options)
      end
    end
  end
end
