module Penguin
end

module Penguin::Helpers
  def active_section?(current_page, section)
    current_page.data.section == section[0]
  end

  def link_to_file(dir, file_id, ext)
    file = "/files/#{dir}/#{data.filenames[file_id]}.#{ext}"
    link_to(ext, file)
  end

  def file_groups(directory)
    directory.split('/').reduce(data.file_groups) do |grouping, directory|
      grouping[directory]
    end
  end
end

