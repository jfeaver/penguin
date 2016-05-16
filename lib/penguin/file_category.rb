module Penguin
  class FileCategory
    include Enumerable

    def initialize(category_data)
      @category_data = category_data
    end

    def each(&block)
      @category_data.each do |group|
        block.call(group) if group[1]&.member?('title')
      end
    end
  end
end
