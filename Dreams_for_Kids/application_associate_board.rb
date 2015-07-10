require "pdfkit"
require "google/api_client"
require 'json'
require "google_drive"


class DreamsForKids

  # This is the class that will handle DKF tasks

  def fetch_form_data_google_drive

    # follow these:
    # http://gimite.net/doc/google-drive-ruby/

    json_file = JSON.parse(File.read("DreamsForKids.json"))

    client = Google::APIClient.new
    auth = client.authorization
    auth.client_id = json_file['native_app_client_id']
    auth.client_secret = json_file['native_app_client_secret']
    auth.scope =
        "https://www.googleapis.com/auth/drive " +
        "https://spreadsheets.google.com/feeds/"
    auth.redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
    print("1. Open this page:\n%s\n\n" % auth.authorization_uri)
    print("2. Enter the authorization code shown in the page: ")
    auth.code = $stdin.gets.chomp
    auth.fetch_access_token!
    access_token = auth.access_token

    # Creates a session.
    session = GoogleDrive.login_with_oauth(access_token)

    # key is in json file
    ws = session.spreadsheet_by_key(json_file['ws_key']).worksheets[0]

    @all_data = ws.rows

    return @all_data

  end

  def number_of_applicants(input_array)
    total_applicants = input_array.length - 1
    puts total_applicants
  end

  def fetch_html_template()
    File.open("member_application_template.html") { |f|
      @html_template = f.read
    }
  end

  def create_applicant_html(options)

    # Creates filenames
    @filename_html = "applications_associate_board/html/#{options[1]}#{options[2]}.html"
    @filename_pdf = "applications_associate_board/pdf/#{options[1]}#{options[2]}.pdf"

    # Use instance variables to replace placeholders in html file

    @html_template.gsub!("a_first_name"){options[1]} # @all_data)[1][1]
    @html_template.gsub!("a_last_name"){options[2]} # @all_data)[1][2]
    @html_template.gsub!("a_mailing_address"){options[3]} # @all_data)[1][3]
    @html_template.gsub!("a_city"){options[4]} # @all_data)[1][4]
    @html_template.gsub!("a_phone_number"){options[6]} # @all_data)[1][6]
    @html_template.gsub!("a_email"){options[7]} # @all_data)[1][7]
    @html_template.gsub!("a_occupation"){options[8]} # @all_data)[1][8]
    @html_template.gsub!("a_1"){options[9]} # @all_data)[1][9]
    @html_template.gsub!("a_2"){options[10]} # @all_data)[1][10]
    @html_template.gsub!("a_3"){options[11]} # @all_data)[1][11]
    @html_template.gsub!("a_4"){options[12]} # @all_data)[1][12]
    @html_template.gsub!("a_5"){options[13]} # @all_data)[1][13]

    # Create instance object so it can be returned and used in class
    @applicant_html = File.open(@filename_html, 'w') { |file| file.write(@html_template) }

  end

  def create_pdf_from_html

    # Creates pdf from html

    kit = PDFKit.new(File.read(@filename_html), :page_size => 'Letter')
    kit.stylesheets << 'default.css'

    # Get an inline PDF
    pdf = kit.to_pdf

    # Save the PDF to a file
    file = kit.to_file(@filename_pdf)

  end

  def main()
    # Combines all functions

    # creates a class to access the fetch data function
    c = DreamsForKids.new
    google_data = c.fetch_form_data_google_drive # ok

    # Loop to unpack data, create html and pdfs for each of the applicants
    # has to create new classes for each iteration, due to variables issues
    google_data.each {|a|
      next if a[1] == "First Name" # skips the header
      d = DreamsForKids.new
      d.fetch_html_template # ok

      # Only creates html if file doesn't exist
      if File.exist?(@filename_html.to_s)
        next
      else
        d.create_applicant_html(a) # ok
      end

      # Only creates pdf if file doesn't exist
      if File.exist?(@filename_pdf.to_s)
        next
      else
        d.create_pdf_from_html
      end

    }

  end

end

new_class = DreamsForKids.new

# Use main() to generate the pdfs
new_class.main()

# # Use this to fetch number of comments
# new_array = new_class.fetch_form_data_google_drive # creates array object with data from sheets
# new_class.number_of_applicants(new_array) # puts to screen method
