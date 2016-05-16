module Penguin
end

module Penguin::Helpers
  def active_section?(current_page, section)
    current_page.data.section == section[0]
  end

  def link_to_file(ext, directory, filename)
    link_to(ext, "/files/#{directory}/#{filename}.#{ext}")
  end

  def file_groups(directory)
    dig_data(directory, data.file_groups)
  end

  def dig_data(directory, the_data)
    directory.split('/').reduce(the_data) do |group, subgroup|
      group[subgroup]
    end
  end
end
