module Penguin
end

module Penguin::Helpers
  def active_section?(current_page, section)
    current_page.data.section == section[0]
  end
end

