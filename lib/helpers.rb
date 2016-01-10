module Penguin
end

module Penguin::Helpers
  def active_section?(current_page, section)
    current_page.data.section == section[0]
  end

  def link_to_file(file_id, content = nil)
    file = "/files/#{data.files[file_id]}"
    content ||= File.basename(file)
    link_to(content, file)
  end
end

